<?xml version="1.0" encoding="utf-8"?>
<Element>
    <Script>
        <Name>PMP\Angular_ANGPLAPEN.py</Name>
        <Title>Angular ANGPLAPEN</Title>
        <Version>1.0</Version>
    </Script>

    <!-- ============================ GEOMETRÍA ============================ -->
    <Page>
        <Name>Geometria</Name>
        <Text>Geometría</Text>

        <Parameter>
            <Name>Length</Name>
            <Text>Longitud (mm)</Text>
            <Value>200</Value>
            <ValueType>Length</ValueType>
            <MinValue>10</MinValue>
        </Parameter>
        <Parameter>
            <Name>LegHorizontal</Name>
            <Text>Ala horizontal A (mm)</Text>
            <Value>100</Value>
            <ValueType>Length</ValueType>
            <MinValue>10</MinValue>
        </Parameter>
        <Parameter>
            <Name>LegVertical</Name>
            <Text>Ala vertical B (mm)</Text>
            <Value>100</Value>
            <ValueType>Length</ValueType>
            <MinValue>10</MinValue>
        </Parameter>
        <Parameter>
            <Name>Thickness</Name>
            <Text>Espesor t (mm)</Text>
            <Value>10</Value>
            <ValueType>Length</ValueType>
            <MinValue>1</MinValue>
        </Parameter>
    </Page>

    <!-- ============================ AGUJEROS ============================= -->
    <Page>
        <Name>Agujeros</Name>
        <Text>Agujeros</Text>

        <Parameter>
            <Name>HoleDiameter</Name>
            <Text>Diámetro agujeros (mm)</Text>
            <Value>18</Value>
            <ValueType>Length</ValueType>
            <!-- Campo solo informativo: no editable (preparado para hacerlo dinámico en el futuro) -->
            <Enable>False</Enable>
        </Parameter>
        <Parameter>
            <Name>HoleLegs</Name>
            <Text>Alas con agujeros</Text>
            <Value>Ambas</Value>
            <ValueList>Ambas|Horizontal|Vertical|Ninguna</ValueList>
            <ValueType>StringComboBox</ValueType>
        </Parameter>
        <Parameter>
            <Name>HolesPerLeg</Name>
            <Text>Nº agujeros por ala</Text>
            <Value>2</Value>
            <ValueType>Integer</ValueType>
            <MinValue>0</MinValue>
            <MaxValue>50</MaxValue>
            <Visible>HoleLegs != "Ninguna"</Visible>
        </Parameter>
        <Parameter>
            <Name>HoleEdgeDistance</Name>
            <Text>Distancia al extremo (mm)</Text>
            <Value>50</Value>
            <ValueType>Length</ValueType>
            <MinValue>0</MinValue>
            <Visible>HoleLegs != "Ninguna"</Visible>
        </Parameter>
        <Parameter>
            <Name>HoleGaugeHorizontal</Name>
            <Text>Gramil ala horizontal (mm, desde el talón)</Text>
            <Value>55</Value>
            <ValueType>Length</ValueType>
            <Visible>HoleLegs == "Ambas" or HoleLegs == "Horizontal"</Visible>
        </Parameter>
        <Parameter>
            <Name>HoleGaugeVertical</Name>
            <Text>Gramil ala vertical (mm, desde el talón)</Text>
            <Value>55</Value>
            <ValueType>Length</ValueType>
            <Visible>HoleLegs == "Ambas" or HoleLegs == "Vertical"</Visible>
        </Parameter>
        <Parameter>
            <Name>HoleCountInfo</Name>
            <Text>Nº total de agujeros</Text>
            <Value>4</Value>
            <ValueType>Integer</ValueType>
            <Enable>False</Enable>
        </Parameter>
    </Page>

    <!-- ============================ ATRIBUTOS ============================ -->
    <Page>
        <Name>Atributos</Name>
        <Text>Atributos</Text>

        <Parameter>
            <Name>ArticleCode</Name>
            <Text>pmp_CARTICULO</Text>
            <Value>FG01_002_012</Value>
            <ValueType>String</ValueType>
            <Enable>False</Enable>
        </Parameter>
        <Parameter>
            <Name>Denomination</Name>
            <Text>DEN</Text>
            <Value>ANGPLAPEN</Value>
            <ValueType>String</ValueType>
            <Enable>False</Enable>
        </Parameter>
        <Parameter>
            <Name>Assembly</Name>
            <Text>Montaje</Text>
            <Value>OBRA</Value>
            <ValueList>OBRA|FABRICA</ValueList>
            <ValueType>StringComboBox</ValueType>
        </Parameter>
        <Parameter>
            <Name>Material</Name>
            <Text>Material</Text>
            <Value>S275</Value>
            <ValueList>S235|S275|S355|CUSTOM</ValueList>
            <ValueType>StringComboBox</ValueType>
        </Parameter>
        <Parameter>
            <Name>MaterialCustom</Name>
            <Text>Material personalizado</Text>
            <Value></Value>
            <ValueType>String</ValueType>
            <Visible>Material == "CUSTOM"</Visible>
        </Parameter>
        <Parameter>
            <Name>FireResistance</Name>
            <Text>Resistencia al fuego</Text>
            <Value>R 30</Value>
            <ValueList>R 0|R 30|R 60|R 90|R 120|R 180</ValueList>
            <ValueType>StringComboBox</ValueType>
        </Parameter>
        <Parameter>
            <Name>WeightInfo</Name>
            <Text>Peso (kg)</Text>
            <Value>0.0</Value>
            <ValueType>Double</ValueType>
            <Enable>False</Enable>
        </Parameter>
    </Page>
</Element>
