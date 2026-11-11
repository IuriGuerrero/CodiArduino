# SmartPart ANGPLAPEN – Pestaña «Parámetros»

Crear estos parámetros en el editor de SmartParts (pestaña *Parámetros*).
Los atributos se asignan enlazando cada parámetro con su atributo Allplan
en la columna **«Atributo»** del diálogo de parámetros (al crear el
parámetro o después). El valor del parámetro se escribe en ese atributo.

Unidades de longitud: mm (ver variable `u` del Master-Script).

| Nombre    | Tipo     | Valor por defecto | Atributo enlazado       | Descripción                              |
|-----------|----------|-------------------|-------------------------|------------------------------------------|
| L         | Longitud | 250               | –                       | Longitud del angular                     |
| A         | Longitud | 120               | –                       | Ala horizontal (superior)                |
| B         | Longitud | 120               | –                       | Ala vertical (colgante)                  |
| t         | Longitud | 12                | –                       | Espesor                                  |
| e         | Longitud | 50                | –                       | Distancia agujero–extremo                |
| g         | Longitud | 80                | –                       | Gramil (talón → eje agujero)             |
| n         | Entero   | 2                 | –                       | Nº agujeros por ala                      |
| d         | Longitud | 12                | PMP_FG_ANG_FORAT_DIAM   | Diámetro agujeros (bloqueado)            |
| muntatge  | Texto    | OBRA              | PMP_FG_ANG_MUNTATGE     | OBRA / FABRICA                           |
| material  | Texto    | S275              | PMP_MATERIAL            | S235 / S275 / S355 / CUSTOM              |
| rf        | Texto    | R 30              | PMP_RESISTENCIA_FOC     | R 0 … R 180                              |
| nforats   | Entero   | 4                 | PMP_FG_ANG_FORATS       | Calculado (bloqueado)                    |
| pes       | Real     | 5.33              | Pes                     | Peso kg, calculado (bloqueado)           |
| carticulo | Texto    | FG01_002_012      | pmp_CARTICULO           | Fijo (bloqueado)                         |
| den       | Texto    | ANGPLAPEN         | DEN                     | Fijo (bloqueado)                         |
