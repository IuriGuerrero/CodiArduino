"""
PythonPart para Allplan 2025: angular L con agujeros (ANGPLAPEN).

Atributos escritos en la PythonPart:
    pmp_CARTICULO          -> FG01_002_012
    DEN                    -> ANGPLAPEN
    PMP_FG_ANG_FORATS      -> número total de agujeros
    Pes                    -> peso en kg (densidad acero 7850 kg/m3)
    PMP_FG_ANG_FORAT_DIAM  -> diámetro de los agujeros (mm)
    PMP_FG_ANG_MUNTATGE    -> OBRA / FABRICA
    PMP_MATERIAL           -> S235 / S275 / S355 / texto libre
    PMP_RESISTENCIA_FOC    -> R 0 ... R 180

Sistema local: talón del angular en el origen, longitud según X,
ala horizontal según Y (A), ala vertical según Z (B).
"""

import math

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements

from BuildingElementAttributeList import BuildingElementAttributeList
from CreateElementResult import CreateElementResult
from PythonPartUtil import PythonPartUtil

STEEL_DENSITY = 7850.0  # kg/m3

ASSEMBLY_OPTIONS = ("OBRA", "FABRICA")
MATERIAL_OPTIONS = ("S235", "S275", "S355", "CUSTOM")
FIRE_OPTIONS = ("R 0", "R 30", "R 60", "R 90", "R 120", "R 180")

# Si GetAttributeID no encuentra un atributo (no definido en el proyecto),
# se usa este número. Rellenar con los IDs reales de vuestros atributos de usuario.
ATTR_ID_FALLBACK = {
    "pmp_CARTICULO": 0,
    "DEN": 0,
    "PMP_FG_ANG_FORATS": 0,
    "Pes": 0,
    "PMP_FG_ANG_FORAT_DIAM": 0,
    "PMP_FG_ANG_MUNTATGE": 0,
    "PMP_MATERIAL": 0,
    "PMP_RESISTENCIA_FOC": 0,
}


def check_allplan_version(_build_ele, _version) -> bool:
    return True


# --------------------------------------------------------------------------- #
#  Cálculos
# --------------------------------------------------------------------------- #
def _hole_legs(build_ele):
    legs = build_ele.HoleLegs.value
    return (legs in ("Ambas", "Horizontal"), legs in ("Ambas", "Vertical"))


def _hole_positions_x(build_ele):
    """Posiciones X de los agujeros a lo largo de la longitud."""
    n = build_ele.HolesPerLeg.value
    length = build_ele.Length.value
    edge = build_ele.HoleEdgeDistance.value
    if n <= 0:
        return []
    if n == 1:
        return [length / 2.0]
    edge = min(edge, length / 2.0)
    step = (length - 2.0 * edge) / (n - 1)
    return [edge + i * step for i in range(n)]


def _hole_count(build_ele) -> int:
    on_h, on_v = _hole_legs(build_ele)
    return len(_hole_positions_x(build_ele)) * (int(on_h) + int(on_v))


def _weight_kg(build_ele) -> float:
    a = build_ele.LegHorizontal.value
    b = build_ele.LegVertical.value
    t = build_ele.Thickness.value
    length = build_ele.Length.value
    r = build_ele.HoleDiameter.value / 2.0

    area = a * t + (b - t) * t                      # mm2 sección L
    volume = area * length                          # mm3
    volume -= _hole_count(build_ele) * math.pi * r * r * t
    return round(max(volume, 0.0) * 1e-9 * STEEL_DENSITY, 2)


def _material(build_ele) -> str:
    mat = build_ele.Material.value.strip()
    if mat == "CUSTOM":
        mat = build_ele.MaterialCustom.value.strip() or "CUSTOM"
    return mat


# --------------------------------------------------------------------------- #
#  Geometría
# --------------------------------------------------------------------------- #
def _cuboid(x, y, z, dx, dy, dz):
    placement = AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(x, y, z),
                                           AllplanGeo.Vector3D(1, 0, 0),
                                           AllplanGeo.Vector3D(0, 0, 1))
    return AllplanGeo.BRep3D.CreateCuboid(placement, dx, dy, dz)


def _cylinder(origin, axis, radius, height):
    ref = AllplanGeo.Vector3D(1, 0, 0) if abs(axis.X) < 0.9 else AllplanGeo.Vector3D(0, 1, 0)
    placement = AllplanGeo.AxisPlacement3D(origin, ref, axis)
    return AllplanGeo.BRep3D.CreateCylinder(placement, radius, height)


def _create_geometry(build_ele):
    a = build_ele.LegHorizontal.value
    b = build_ele.LegVertical.value
    t = build_ele.Thickness.value
    length = build_ele.Length.value
    r = build_ele.HoleDiameter.value / 2.0

    horizontal = _cuboid(0, 0, 0, length, a, t)
    vertical = _cuboid(0, 0, 0, length, t, b)
    err, solid = AllplanGeo.MakeUnion(horizontal, vertical)
    if err:
        solid = horizontal

    on_h, on_v = _hole_legs(build_ele)
    over = 1.0
    for x in _hole_positions_x(build_ele):
        if on_h:
            y = build_ele.HoleGaugeHorizontal.value
            cyl = _cylinder(AllplanGeo.Point3D(x, y, -over),
                            AllplanGeo.Vector3D(0, 0, 1), r, t + 2 * over)
            err, res = AllplanGeo.MakeSubtraction(solid, cyl)
            if not err:
                solid = res
        if on_v:
            z = build_ele.HoleGaugeVertical.value
            cyl = _cylinder(AllplanGeo.Point3D(x, -over, z),
                            AllplanGeo.Vector3D(0, 1, 0), r, t + 2 * over)
            err, res = AllplanGeo.MakeSubtraction(solid, cyl)
            if not err:
                solid = res
    return solid


# --------------------------------------------------------------------------- #
#  Atributos
# --------------------------------------------------------------------------- #
def _attr_id(doc, name) -> int:
    try:
        attr_id = AllplanBaseElements.AttributeService.GetAttributeID(doc, name)
    except Exception:  # pylint: disable=broad-except
        attr_id = -1
    if attr_id is None or attr_id <= 0:
        attr_id = ATTR_ID_FALLBACK.get(name, 0)
    return attr_id


def _create_attributes(build_ele, doc) -> BuildingElementAttributeList:
    values = {
        "pmp_CARTICULO": build_ele.ArticleCode.value,
        "DEN": build_ele.Denomination.value,
        "PMP_FG_ANG_FORATS": int(_hole_count(build_ele)),
        "Pes": float(_weight_kg(build_ele)),
        "PMP_FG_ANG_FORAT_DIAM": float(build_ele.HoleDiameter.value),
        "PMP_FG_ANG_MUNTATGE": build_ele.Assembly.value,
        "PMP_MATERIAL": _material(build_ele),
        "PMP_RESISTENCIA_FOC": build_ele.FireResistance.value,
    }
    attr_list = BuildingElementAttributeList()
    for name, value in values.items():
        attr_id = _attr_id(doc, name)
        if attr_id > 0:
            attr_list.add_attribute(attr_id, value)
        else:
            print(f"[ANGPLAPEN] Atributo '{name}' no definido en el proyecto: no se escribe.")
    return attr_list


# --------------------------------------------------------------------------- #
#  Entradas de Allplan
# --------------------------------------------------------------------------- #
def _update_info_fields(build_ele):
    build_ele.HoleCountInfo.value = _hole_count(build_ele)
    build_ele.WeightInfo.value = _weight_kg(build_ele)


def create_element(build_ele, doc) -> CreateElementResult:
    _update_info_fields(build_ele)

    com_prop = AllplanBaseElements.CommonProperties()
    com_prop.GetGlobalProperties()

    model_ele = AllplanBasisElements.ModelElement3D(com_prop, _create_geometry(build_ele))

    pyp_util = PythonPartUtil()
    pyp_util.add_pythonpart_view_2d3d(model_ele)
    pyp_util.add_attribute_list(_create_attributes(build_ele, doc))

    return CreateElementResult(pyp_util.create_pythonpart(build_ele))


def modify_element_property(build_ele, name, value) -> bool:
    # Los combos de montaje y resistencia al fuego solo admiten sus opciones.
    if name == "Assembly" and value not in ASSEMBLY_OPTIONS:
        build_ele.Assembly.value = "OBRA"
    elif name == "FireResistance" and value not in FIRE_OPTIONS:
        build_ele.FireResistance.value = "R 30"
    # Material: si se escribe un texto libre en el combo, se acepta tal cual.

    # Limitar el espesor para que la geometría sea válida
    t_max = min(build_ele.LegHorizontal.value, build_ele.LegVertical.value) - 1.0
    if build_ele.Thickness.value > t_max:
        build_ele.Thickness.value = t_max

    _update_info_fields(build_ele)
    return True
