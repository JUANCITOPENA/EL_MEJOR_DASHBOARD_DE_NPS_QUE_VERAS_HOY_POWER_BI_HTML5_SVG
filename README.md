# 🦁 Dashboard Ejecutivo NPS: Banca & Telecomunicaciones (Premium UI)

> **Versión:** 2.0 (High Performance Edition)  
> **Tecnología:** Power BI + DAX + HTML5/SVG + Python  
> **Enfoque:** Visualización de Datos Avanzada (Custom Visuals via DAX)  
> **Estado:** 🟢 Producción

---

## 📖 1. Narrativa y Contexto del Negocio

### 🏦 El Escenario
**"Banca Claro RD"** es una institución líder que busca monitorear la satisfacción de sus clientes (NPS) en tiempo real. La alta dirección requiere un tablero que no solo muestre números, sino que **transmita el éxito y la excelencia** de la gestión actual.

### 🚩 El Problema (Pain Point)
Los visuales nativos de Power BI (tacómetros estándar, gráficos de barras simples) eran insuficientes para:
1.  **Impacto Visual:** Se veían "planos" y poco corporativos.
2.  **Flexibilidad:** No permitían zonas de colores personalizadas ni iconos dinámicos.
3.  **Narrativa:** No contaban la historia de la demografía del cliente de un vistazo.

### 🚀 La Solución
Se desarrolló una arquitectura híbrida donde **Power BI procesa los datos** y **DAX genera código HTML/SVG dinámico**. Esto permite crear tarjetas visuales de "calidad web" (pixel-perfect) que reaccionan a los filtros, mostrando una interfaz limpia, moderna y altamente estética.

---

## 🛠️ 2. Arquitectura de Datos (Backend)

Para simular un escenario real y garantizar que los KPIs reflejen una gestión exitosa, se generó un **Dataset Sintético Calibrado** utilizando Python.

### 🐍 Generación de Datos (Python Script)
Se creó una base de datos `nps_dataset_rd_banca_claro` con **5,000 registros** y las siguientes características:

*   **Periodo:** 3 años de histórico.
*   **Cobertura:** Nacional (Regiones Ozama, Cibao, Sur, Este).
*   **Segmentación:** Sexo, Rango de Edad (calculado dinámicamente), Plan, Gerente.
*   **Calibración Positiva (The "Winner" Logic):**
    *   🟩 **Promotores (9-10):** ~78% (Mayoría absoluta).
    *   🟨 **Neutros (7-8):** ~8% (Minimizado).
    *   🟥 **Detractores (0-6):** ~14% (Controlado).

---

## 🧠 3. Lógica de Negocio y KPIs (DAX)

Las medidas no son simples sumas; contienen lógica de negocio para determinar el "Color del Éxito".

### 📊 Indicadores Clave (KPIs)

| Indicador | Definición | Meta / Regla de Negocio |
| :--- | :--- | :--- |
| **NPS Score** | `(Promotores % - Detractores %) * 100` | > 50 (Excelente) |
| **% Promotores** | `Total Promotores / Total Respuestas` | **Si es > 70%, se fuerza el ESTADO VERDE.** |
| **Zona de Clasificación** | Texto dinámico según el Score | Excelencia, Calidad, Mejora, Crítica. |

---

## 🎨 4. Visualización Avanzada (Frontend)

El corazón del reporte son dos medidas DAX complejas que renderizan HTML5 puro dentro de Power BI usando el visual "HTML Content".

### 1️⃣ Tarjeta NPS (Velocímetro SVG)
Un componente visual complejo diseñado a medida que incluye:

*   **Gauge Semicircular (SVG):** Dibuja un arco de 180° dinámico y nítido.
*   **Aguja Rotatoria:** Calcula el ángulo exacto basado en el NPS (Escala de -100 a 100).
    *   *Fórmula de rotación:* `INT(MAX(0, MIN(180, (_NPS + 100) * 0.9)))`
*   **Indicadores de Segmento:** Barras de progreso inferiores con iconos vectoriales (SVG path) que cambian de color según el segmento.
*   **Clean UI:** Se eliminaron botones innecesarios para ofrecer una vista ejecutiva limpia.

### 2️⃣ Tarjeta Perfil del Cliente (Demografía)
Un panel informativo que desglosa quién está respondiendo la encuesta:

*   **Iconos de Género:** Vectores SVG que cambian dinámicamente según el sexo predominante.
*   **Barras Apiladas (CSS Grid):**
    *   Muestra la distribución de edad (18-29, 30-39, etc.).
    *   Utiliza barras bicolores (Rosa/Azul Oscuro) dentro del mismo contenedor visual.
*   **Técnica Web:** Uso de `width: %` en divs HTML calculados via DAX.
*   **Corrección de Error:** Se usa la columna numérica `[Idade]` para calcular los rangos "al vuelo", evitando errores de dependencias circulares.

---

## 🚦 5. Zonas de Gestión (Semáforo)

El dashboard clasifica automáticamente el desempeño del Gerente o Región en 4 zonas de actuación:

*   🏆 **Zona de Excelencia:** NPS > 75 **o** Promotores > 70%. *(Color: Verde Neón / #00E676)*.
*   ✅ **Zona de Calidad:** NPS entre 50 y 75. *(Color: Verde Medio / #00E676)*.
*   ⚠️ **Zona de Mejora:** NPS positivo pero bajo (< 50). *(Color: Amarillo-Dorado / #F4B400)*.
*   ⛔ **Zona Crítica:** NPS Negativo. *(Color: Rojo-Rosa / #E91E63)*.

---

## 📦 6. Instalación y Uso

### Pasos para desplegar:
1.  **Fuente de Datos:** Cargar el archivo generado `nps_dataset_rd_banca_claro.xlsx`.
2.  **Custom Visual:** Importar el visual **"HTML Content"** (de Daniel Marsh-Patrick) desde AppSource.
3.  **Medidas Base:** Crear todas las medidas detalladas en la Sección 7.
4.  **Visuales Avanzados:**
    *   Arrastrar la medida `[HTML_NPS_Card]` al lienzo para ver el velocímetro.
    *   Arrastrar la medida `[HTML_Perfil_Premium]` al lienzo para ver la demografía.
5.  **Interacción:** Al filtrar por *Gerente*, *Año* o *Región*, ambos visuales recalculan sus vectores y colores instantáneamente.

---

## 💻 7. Repositorio de Medidas DAX (Código Fuente)

### 📌 7.1 Columnas Calculadas
> **Importante:** Crear como "Nueva Columna" en la tabla `nps_dataset_rd_banca_claro`.

```dax
Rango_Edad = 
SWITCH( TRUE(),
    'nps_dataset_rd_banca_claro'[Idade] <= 24, "18-24",
    'nps_dataset_rd_banca_claro'[Idade] <= 34, "25-34",
    'nps_dataset_rd_banca_claro'[Idade] <= 44, "35-44",
    'nps_dataset_rd_banca_claro'[Idade] <= 54, "45-54",
    'nps_dataset_rd_banca_claro'[Idade] <= 64, "55-64",
    "65+"
)
```

### 📌 7.2 Medidas Base (Totales)

```dax
Total Respuestas = 
COUNTROWS ( nps_dataset_rd_banca_claro )

Total Promotores = 
CALCULATE (
    COUNTROWS ( nps_dataset_rd_banca_claro ),
    nps_dataset_rd_banca_claro[NPS_Score] >= 9
)

Total Neutros = 
CALCULATE (
    COUNTROWS ( nps_dataset_rd_banca_claro ),
    nps_dataset_rd_banca_claro[NPS_Score] >= 7,
    nps_dataset_rd_banca_claro[NPS_Score] <= 8
)

Total Detractores = 
CALCULATE (
    COUNTROWS ( nps_dataset_rd_banca_claro ),
    nps_dataset_rd_banca_claro[NPS_Score] <= 6
)
```

### 📌 7.3 KPIs y Lógica de Negocio

```dax
NPS Score = 
VAR P = [Total Promotores]
VAR D = [Total Detractores]
VAR T = [Total Respuestas]
RETURN
IF ( T = 0, BLANK(), DIVIDE ( P - D, T ) * 100 )

Pct Promotores = FORMAT ( DIVIDE ( [Total Promotores], [Total Respuestas] ), "0.0%" )
Pct Neutros = FORMAT ( DIVIDE ( [Total Neutros], [Total Respuestas] ), "0.0%" )
Pct Detractores = FORMAT ( DIVIDE ( [Total Detractores], [Total Respuestas] ), "0.0%" )
```

### 🔹 7.4 Visual Avanzado: Tarjeta NPS (HTML_NPS_Card)
*Renderiza el velocímetro, la aguja dinámica y los KPIs inferiores.*

```dax
HTML_NPS_Card = 
-- 1. CÁLCULOS DE BASE
VAR _Total = COUNTROWS('nps_dataset_rd_banca_claro')
VAR _Promotores = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Promotor")
VAR _Neutros = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Neutro")
VAR _Detractores = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Detractor")

-- Cálculo NPS Score
VAR _NPS_Raw = IF(_Total > 0, DIVIDE(_Promotores - _Detractores, _Total) * 100, 0)

-- 2. REGLA ESPECIAL DEL 70% PROMOTORES
VAR _PctProm_Num = DIVIDE(_Promotores, _Total, 0)
VAR _EsTopPerformance = _PctProm_Num >= 0.70

-- 3. LÓGICA DE COLOR Y TEXTO
VAR _Color = 
    SWITCH(TRUE(),
        _EsTopPerformance, "#00E676",  -- ¡FORZAR VERDE!
        _NPS_Raw >= 75, "#00E676",
        _NPS_Raw >= 50, "#00E676",
        _NPS_Raw >= 0,  "#F4B400",
        "#E91E63"
    )

VAR _TextoZona = 
    SWITCH(TRUE(),
        _EsTopPerformance, "Zona de Excelencia",
        _NPS_Raw >= 75, "Zona de Excelencia",
        _NPS_Raw >= 50, "Zona de Calidad",
        _NPS_Raw >= 0,  "Zona de Mejora",
        "Zona Crítica"
    )

-- 4. ÁNGULO DEL GAUGE
VAR _Angulo = INT(MAX(0, MIN(180, DIVIDE(_NPS_Raw + 100, 200) * 180)))

-- 5. FORMATOS
VAR _PctProm_Txt = FORMAT(DIVIDE(_Promotores, _Total), "0%")
VAR _PctNeu_Txt = FORMAT(DIVIDE(_Neutros, _Total), "0%")
VAR _PctDet_Txt = FORMAT(DIVIDE(_Detractores, _Total), "0%")

-- 6. ICONOS DINÁMICOS POR SEXO
VAR _SexoSel = SELECTEDVALUE('nps_dataset_rd_banca_claro'[Sexo], "Todos")
VAR _IconPath = 
    SWITCH(_SexoSel,
        "Femenino", "M12,4A2,2 0 0,1 14,6C14,7.1 13.1,8 12,8A2,2 0 0,1 10,6C10,4.9 10.9,4 12,4M17,12V10H7V12H9V21H11V14H13V21H15V12H17Z",
        "Masculino", "M9,14H15V21H13V16H11V21H9V14M12,12C14.21,12 16,10.21 16,8C16,5.79 14.21,4 12,4C9.79,4 8,5.79 8,8C8,10.21 9.79,12 12,12M18,14V10H6V14H8V24H16V14H18Z",
        "M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"
    )

RETURN
"
<div style='font-family: Segoe UI, sans-serif; background: white; padding: 20px; border-radius: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); width: 100%; height: 100%; box-sizing: border-box; position: relative;'>

    <div style='display: flex; justify-content: center; align-items: center; margin-bottom: 5px;'>
        <div style='text-align: center;'>
            <div style='color: #333; font-size: 16px; font-weight: 600;'>Zona de Classificação (NPS)</div>
            <div style='font-size: 14px; font-weight: bold; color: #ccc; margin-top: 2px;'>00</div>
        </div>
    </div>

    <div style='position: relative; height: 160px; margin: 10px auto; width: 260px;'>
        <svg viewBox='0 0 240 140' style='width: 100%; overflow: visible;'>
            <path d='M 20 120 A 100 100 0 0 1 220 120' fill='none' stroke='#E0E0E0' stroke-width='15' stroke-dasharray='2 5'></path>
            <path d='M 35 120 A 85 85 0 0 1 205 120' fill='none' stroke='" & _Color & "' stroke-width='3'></path>
            <g transform='rotate(" & _Angulo & " 120 120)'>
                 <polygon points='35,120 50,114 50,126' fill='" & _Color & "' transform='rotate(180 42 120)'></polygon>
            </g>
            <text x='15' y='110' font-size='12' fill='#555' font-weight='bold' text-anchor='middle'>-100</text>
            <text x='225' y='110' font-size='12' fill='#555' font-weight='bold' text-anchor='middle'>100</text>
            <text x='188' y='55' font-size='10' fill='#999' font-weight='bold'>50</text>
            <text x='208' y='85' font-size='10' fill='#999' font-weight='bold'>75</text>
        </svg>

        <div style='position: absolute; top: 75%; left: 50%; transform: translate(-50%, -50%); text-align: center;'>
            <div style='font-size: 56px; font-weight: bold; color: " & _Color & "; line-height: 1; text-shadow: 0 2px 5px rgba(0,0,0,0.1);'>" & FORMAT(_NPS_Raw, "0") & "</div>
            <div style='font-size: 16px; font-weight: 700; color: #444; margin-top: 5px; white-space: nowrap;'>" & _TextoZona & "</div>
            <div style='font-size: 13px; color: #999; font-weight: 600;'>NPS</div>
        </div>
    </div>

    <div style='text-align: center; margin-top: 5px;'>
        <div style='font-size: 36px; font-weight: 800; color: #2C3E50;'>" & FORMAT(_Total, "#,##0") & "</div>
        <div style='font-size: 14px; color: #7f8c8d; font-weight: 600;'>Qtde respuestas</div>
    </div>

    <div style='width: 80%; height: 10px; border-top: 2px solid #2C3E50; border-radius: 50% 50% 0 0; margin: 10px auto 20px auto; opacity: 0.1;'></div>

    <div style='display: flex; justify-content: space-between; padding: 0 10px;'>
        <div style='flex: 1; text-align: center;'>
            <div style='font-size: 16px; font-weight: 800; color: #333; margin-bottom: 5px;'>" & _PctDet_Txt & "</div>
            <div style='height: 40px; display: flex; justify-content: center; align-items: end;'>
                 <svg width='40' height='35' viewBox='0 0 24 24' fill='#E91E63' style='filter: drop-shadow(0 4px 6px rgba(233,30,99,0.4));'>
                    <path d='" & _IconPath & "' transform='scale(1.1)'/>
                 </svg>
            </div>
            <div style='font-size: 20px; font-weight: 800; color: #333; margin-top: 5px;'>" & FORMAT(_Detractores, "#,##0") & "</div>
            <div style='font-size: 11px; color: #777; font-weight: 600;'>Detratores</div>
            <div style='height: 4px; width: 30px; background: #E91E63; margin: 5px auto; border-radius: 2px;'></div>
        </div>

        <div style='flex: 1; text-align: center;'>
            <div style='font-size: 16px; font-weight: 800; color: #333; margin-bottom: 5px;'>" & _PctNeu_Txt & "</div>
             <div style='height: 40px; display: flex; justify-content: center; align-items: end;'>
                 <svg width='40' height='35' viewBox='0 0 24 24' fill='#F4B400' style='filter: drop-shadow(0 4px 6px rgba(244,180,0,0.4));'>
                    <path d='" & _IconPath & "' transform='scale(1.1)'/>
                 </svg>
            </div>
            <div style='font-size: 20px; font-weight: 800; color: #333; margin-top: 5px;'>" & FORMAT(_Neutros, "#,##0") & "</div>
            <div style='font-size: 11px; color: #777; font-weight: 600;'>Neutros</div>
            <div style='height: 4px; width: 30px; background: #F4B400; margin: 5px auto; border-radius: 2px;'></div>
        </div>

        <div style='flex: 1; text-align: center;'>
            <div style='font-size: 16px; font-weight: 800; color: #333; margin-bottom: 5px;'>" & _PctProm_Txt & "</div>
             <div style='height: 40px; display: flex; justify-content: center; align-items: end;'>
                 <svg width='40' height='35' viewBox='0 0 24 24' fill='#00E676' style='filter: drop-shadow(0 4px 6px rgba(0,230,118,0.4));'>
                    <path d='" & _IconPath & "' transform='scale(1.1)'/>
                 </svg>
            </div>
            <div style='font-size: 20px; font-weight: 800; color: #333; margin-top: 5px;'>" & FORMAT(_Promotores, "#,##0") & "</div>
            <div style='font-size: 11px; color: #777; font-weight: 600;'>Promotores</div>
            <div style='height: 4px; width: 30px; background: #00E676; margin: 5px auto; border-radius: 2px;'></div>
        </div>
    </div>
</div>
"
```

### 🔹 7.5 Visual Avanzado: Perfil Demográfico (HTML_Perfil_Premium)
*Renderiza las barras de progreso por edad y los iconos de género.*

```dax
HTML_Perfil_Premium = 
VAR _Total = COUNTROWS(nps_dataset_rd_banca_claro)
VAR _Masc = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Sexo] = "Masculino") + 0
VAR _Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _PctMascTxt = FORMAT(DIVIDE(_Masc, _Total), "0%")
VAR _PctFemTxt = FORMAT(DIVIDE(_Fem, _Total), "0%")
VAR _ColorMasc = "#0F1626"
VAR _ColorFem = "#E91E63"

-- CÁLCULOS DE GRUPOS (USANDO 'Idade')
VAR _R1_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 18, nps_dataset_rd_banca_claro[Idade] <= 29) + 0
VAR _R1_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 18, nps_dataset_rd_banca_claro[Idade] <= 29, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R1_Masc = _R1_Tot - _R1_Fem

VAR _R2_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 30, nps_dataset_rd_banca_claro[Idade] <= 39) + 0
VAR _R2_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 30, nps_dataset_rd_banca_claro[Idade] <= 39, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R2_Masc = _R2_Tot - _R2_Fem

VAR _R3_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 40, nps_dataset_rd_banca_claro[Idade] <= 49) + 0
VAR _R3_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 40, nps_dataset_rd_banca_claro[Idade] <= 49, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R3_Masc = _R3_Tot - _R3_Fem

VAR _R4_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 50, nps_dataset_rd_banca_claro[Idade] <= 59) + 0
VAR _R4_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 50, nps_dataset_rd_banca_claro[Idade] <= 59, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R4_Masc = _R4_Tot - _R4_Fem

VAR _R5_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 60) + 0
VAR _R5_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 60, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R5_Masc = _R5_Tot - _R5_Fem

-- ESCALA MÁXIMA
VAR _MaxVal = MAXX({_R1_Tot, _R2_Tot, _R3_Tot, _R4_Tot, _R5_Tot}, [Value])
VAR _Denom = IF(_MaxVal = 0, 1, _MaxVal) * 1.2

-- CÁLCULO DE ANCHOS (%)
VAR _W_R1_F = INT(DIVIDE(_R1_Fem, _Denom, 0) * 100)
VAR _W_R1_M = INT(DIVIDE(_R1_Masc, _Denom, 0) * 100)
VAR _W_R2_F = INT(DIVIDE(_R2_Fem, _Denom, 0) * 100)
VAR _W_R2_M = INT(DIVIDE(_R2_Masc, _Denom, 0) * 100)
VAR _W_R3_F = INT(DIVIDE(_R3_Fem, _Denom, 0) * 100)
VAR _W_R3_M = INT(DIVIDE(_R3_Masc, _Denom, 0) * 100)
VAR _W_R4_F = INT(DIVIDE(_R4_Fem, _Denom, 0) * 100)
VAR _W_R4_M = INT(DIVIDE(_R4_Masc, _Denom, 0) * 100)
VAR _W_R5_F = INT(DIVIDE(_R5_Fem, _Denom, 0) * 100)
VAR _W_R5_M = INT(DIVIDE(_R5_Masc, _Denom, 0) * 100)

RETURN
"
<div style='font-family: Segoe UI, sans-serif; background: #EFEFEF; padding: 15px; border-radius: 15px; display: flex; width: 100%; height: 100%; gap: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); overflow:hidden;'>
    <div style='flex: 1; background: #fff; border-radius: 15px; padding: 10px; display: flex; flex-direction: column; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05); min-width: 180px;'>
        <div style='text-align: center; font-weight: bold; color: #1A237E; margin-bottom: 15px; font-size: 14px;'>Qtde de Resposta por Sexo</div>
        <div style='display: flex; align-items: center; margin-bottom: 20px;'>
            <svg width='50' height='50' viewBox='0 0 24 24'><path d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z' fill='" & _ColorMasc & "'/></svg>
            <div style='margin-left: 10px;'>
                <div style='font-size: 22px; font-weight: 800; color: #333;'>" & _PctMascTxt & "</div>
                <div style='font-size: 11px; font-weight: bold; color: #333;'>Clientes: " & _Masc & "</div>
            </div>
        </div>
        <div style='display: flex; align-items: center;'>
             <svg width='50' height='50' viewBox='0 0 24 24'>
                <path d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z' fill='" & _ColorFem & "'/>
                <path d='M12 8.5c-1.5 0-2.8.8-3.5 2 .5 2 2 3.5 3.5 3.5s3-1.5 3.5-3.5c-.7-1.2-2-2-3.5-2z' fill='#fff' opacity='0.3'/> 
            </svg>
            <div style='margin-left: 10px;'>
                <div style='font-size: 22px; font-weight: 800; color: #333;'>" & _PctFemTxt & "</div>
                <div style='font-size: 11px; font-weight: bold; color: #333;'>Clientes: " & _Fem & "</div>
            </div>
        </div>
    </div>
    <div style='flex: 1.5; background: #fff; border-radius: 15px; padding: 15px; display: flex; flex-direction: column; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.05);'>
        <div style='text-align: center; font-weight: bold; color: #1A237E; margin-bottom: 15px; font-size: 13px;'>Qtde Respostas por Range Idade e Sexo</div>
        
        <!-- RANGO 1 -->
        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>18 a 29</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R1_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R1_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R1_Tot & "</div>
        </div>

        <!-- RANGO 2 -->
        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>30 a 39</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R2_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R2_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R2_Tot & "</div>
        </div>

        <!-- RANGO 3 -->
        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>40 a 49</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R3_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R3_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R3_Tot & "</div>
        </div>

        <!-- RANGO 4 -->
        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>50 a 59</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R4_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R4_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R4_Tot & "</div>
        </div>

        <!-- RANGO 5 -->
        <div style='display: flex; align-items: center;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>acima 59</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R5_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R5_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R5_Tot & "</div>
        </div>
    </div>
</div>
"
```

---

## 🐍 8. Script Python: Generador de Datos Calibrado

Utiliza este script para generar el archivo `nps_dataset_rd_banca_claro.xlsx`.

```python
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# --- CONFIGURACIÓN ---
num_records_random = 5000 

gerentes = [
    'Juliana Gómez', 'Claudia Méndez', 'William Paredes', 'Angela Torres',
    'Gilmar Rodríguez', 'Sandro Valdez', 'Marcos Batista',
    'Patricia Núñez', 'Esteban Jiménez', 'Verónica López'
]

planos = ['Prepago', 'Postpago', 'Empresarial', 'Premium']
lista_sexos = ['Masculino', 'Femenino']

temas_clientes = [
    'Apertura de cuenta bancaria',
    'Préstamo personal aprobado',
    'Tarjeta de crédito',
    'Reclamo resuelto satisfactoriamente',
    'Migración a plan Claro Postpago',
    'Instalación de fibra óptica Claro',
    'Renovación de contrato',
    'Mejora de señal móvil',
    'Actualización de datos',
    'Solicitud empresarial',
    'Atención VIP',
    'Consulta de balance',
    'Pago electrónico exitoso'
]

# --- GEOGRAFÍA REPÚBLICA DOMINICANA ---
dr_locations = [
    {'Region': 'Ozama', 'Provincia': 'Distrito Nacional', 'Ciudad': 'Santo Domingo de Guzmán', 'Weight': 0.18},
    {'Region': 'Ozama', 'Provincia': 'Santo Domingo', 'Ciudad': 'Santo Domingo Este', 'Weight': 0.10},
    {'Region': 'Ozama', 'Provincia': 'Santo Domingo', 'Ciudad': 'Santo Domingo Norte', 'Weight': 0.08},
    {'Region': 'Ozama', 'Provincia': 'Santo Domingo', 'Ciudad': 'Santo Domingo Oeste', 'Weight': 0.06},
    {'Region': 'Norte', 'Provincia': 'Santiago', 'Ciudad': 'Santiago de los Caballeros', 'Weight': 0.12},
    {'Region': 'Norte', 'Provincia': 'La Vega', 'Ciudad': 'La Vega', 'Weight': 0.05},
    {'Region': 'Norte', 'Provincia': 'Duarte', 'Ciudad': 'San Francisco de Macorís', 'Weight': 0.05},
    {'Region': 'Norte', 'Provincia': 'Puerto Plata', 'Ciudad': 'Puerto Plata', 'Weight': 0.04},
    {'Region': 'Norte', 'Provincia': 'Espaillat', 'Ciudad': 'Moca', 'Weight': 0.03},
    {'Region': 'Este', 'Provincia': 'La Altagracia', 'Ciudad': 'Higüey', 'Weight': 0.05},
    {'Region': 'Este', 'Provincia': 'La Altagracia', 'Ciudad': 'Punta Cana', 'Weight': 0.07},
    {'Region': 'Este', 'Provincia': 'La Romana', 'Ciudad': 'La Romana', 'Weight': 0.04},
    {'Region': 'Este', 'Provincia': 'San Pedro de Macorís', 'Ciudad': 'San Pedro de Macorís', 'Weight': 0.04},
    {'Region': 'Sur', 'Provincia': 'San Cristóbal', 'Ciudad': 'San Cristóbal', 'Weight': 0.05},
    {'Region': 'Sur', 'Provincia': 'Peravia', 'Ciudad': 'Baní', 'Weight': 0.03},
    {'Region': 'Sur', 'Provincia': 'Barahona', 'Ciudad': 'Barahona', 'Weight': 0.03},
    {'Region': 'Sur', 'Provincia': 'Azua', 'Ciudad': 'Azua', 'Weight': 0.03}
]

loc_weights = [l['Weight'] for l in dr_locations]

data = []

# --- FECHAS ---
start_date = datetime(2023, 1, 1)
total_days = 365 * 3

print("Generando estructura base...")

# FASE 1 – Estructura base (Anti-Huecos)
edades_base = [25, 35, 45, 55, 65]
for gerente in gerentes:
    for score in range(11):
        for edad in edades_base:
            for sexo in lista_sexos:
                fecha = start_date + timedelta(days=random.randint(0, total_days))
                loc = random.choice(dr_locations)

                if score >= 9: clasificacion = 'Promotor'
                elif score >= 7: clasificacion = 'Neutro'
                else: clasificacion = 'Detractor'

                data.append([
                    len(data) + 1, fecha, fecha.year, gerente, sexo, random.choice(planos),
                    loc['Region'], loc['Provincia'], loc['Ciudad'], score, clasificacion,
                    edad + random.randint(-2, 2), random.choice(temas_clientes)
                ])

print("Generando volumen positivo...")

# FASE 2 – Volumen Calibrado (Promotores > 75%)
probs = np.array([
    0.01, 0.01, 0.01, 0.02, 0.02, 0.03, 0.04,  
    0.02, 0.04,                                
    0.35, 0.45                                 
])
probs = probs / probs.sum()

for _ in range(num_records_random):
    fecha = start_date + timedelta(days=random.randint(0, total_days))
    loc = random.choices(dr_locations, weights=loc_weights, k=1)[0]
    score = np.random.choice(np.arange(0, 11), p=probs)

    if score >= 9: clasificacion = 'Promotor'
    elif score >= 7: clasificacion = 'Neutro'
    else: clasificacion = 'Detractor'

    data.append([
        len(data) + 1, fecha, fecha.year, random.choice(gerentes), random.choice(lista_sexos),
        random.choice(planos), loc['Region'], loc['Provincia'], loc['Ciudad'], score,
        clasificacion, random.randint(18, 75), random.choice(temas_clientes)
    ])

# --- EXPORTAR ---
cols = [
    'ID', 'Fecha', 'Ano', 'Gerente', 'Sexo', 'Plano', 
    'Region', 'Estado', 'Ciudad', 
    'NPS_Score', 'Clasificacion', 'Idade', 'Tema_Cliente'
]

df = pd.DataFrame(data, columns=cols)

archivo = "nps_dataset_rd_banca_claro.xlsx"
df.to_excel(archivo, index=False)
print(f"✅ Archivo generado sin conflictos: {archivo}")
```
