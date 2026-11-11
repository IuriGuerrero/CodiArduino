# SmartPart ANGPLAPEN – Pestaña «Parámetros»

Crear estos parámetros en el editor de SmartParts (pestaña *Parámetros*).
Unidades de longitud: mm (ver variable `u` del Master-Script).

| Nombre      | Tipo     | Valor por defecto | Descripción                                   |
|-------------|----------|-------------------|-----------------------------------------------|
| L           | Longitud | 250               | Longitud del angular                          |
| A           | Longitud | 120               | Ala horizontal (superior)                     |
| B           | Longitud | 120               | Ala vertical (colgante)                       |
| t           | Longitud | 12                | Espesor                                       |
| e           | Longitud | 50                | Distancia del primer/último agujero al extremo|
| g           | Longitud | 80                | Gramil: distancia del talón al eje del agujero|
| n           | Entero   | 2                 | Nº de agujeros por ala                        |
| d           | Longitud | 12                | Diámetro agujeros (NO editable, LOCK)         |
| muntatge    | Texto    | OBRA              | OBRA / FABRICA                                |
| material    | Texto    | S275              | S235 / S275 / S355 / CUSTOM (texto libre)     |
| rf          | Texto    | R 30              | R 0 … R 180                                   |
| nforats     | Entero   | 4                 | Calculado (no editable)                       |
| pes         | Real     | 0                 | Calculado en kg (no editable)                 |

## Atributos Allplan

Para cada atributo, crear un parámetro adicional cuyo **nombre sea el número
del atributo entre arrobas** (`@nnnn@`), que es como el SmartPart transfiere
valores a atributos Allplan. Sustituir `nnnn` por el número que tenga cada
atributo de usuario en vuestro proyecto (Gestor de atributos) y cambiar los
mismos números en el Parameter-Script.

| Atributo              | Parámetro (ejemplo) | Tipo   | Valor                 |
|-----------------------|---------------------|--------|-----------------------|
| pmp_CARTICULO         | @nnn1@              | Texto  | FG01_002_012          |
| DEN                   | @nnn2@              | Texto  | ANGPLAPEN             |
| PMP_FG_ANG_FORATS     | @nnn3@              | Entero | = nforats             |
| Pes                   | @nnn4@              | Real   | = pes                 |
| PMP_FG_ANG_FORAT_DIAM | @nnn5@              | Real   | = d                   |
| PMP_FG_ANG_MUNTATGE   | @nnn6@              | Texto  | = muntatge            |
| PMP_MATERIAL          | @nnn7@              | Texto  | = material            |
| PMP_RESISTENCIA_FOC   | @nnn8@              | Texto  | = rf                  |

Marcar estos parámetros como ocultos (no aparecen en el diálogo).
