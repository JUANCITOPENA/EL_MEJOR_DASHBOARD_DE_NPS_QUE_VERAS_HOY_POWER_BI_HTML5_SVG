# 🦁 Dashboard Ejecutivo NPS: Banca & Telecomunicaciones (Premium UI)

> **Versión:** 2.0 (High Performance Edition)  
> **Tecnología:** Power BI + DAX + HTML5/SVG + Python  
> **Enfoque:** Visualización de Datos Avanzada (Custom Visuals via DAX)  
> **Estado:** 🟢 Producción

---


## Presetancion:

![Portada](portada.png)



## 📑 Tabla de Contenido (Menú)

1.  [Narrativa y Contexto del Negocio](#-1-narrativa-y-contexto-del-negocio)
2.  [Arquitectura de Datos (Backend)](#-2-arquitectura-de-datos-backend)
3.  [Lógica de Negocio y KPIs (DAX)](#-3-lógica-de-negocio-y-kpis-dax)
4.  [Visualización Avanzada (Frontend)](#-4-visualización-avanzada-frontend)
5.  [Zonas de Gestión (Semáforo)](#-5-zonas-de-gestión-semáforo)
6.  [Instalación y Uso](#-6-instalación-y-uso)
7.  [Repositorio de Medidas DAX (Documentación Técnica)](#-7-repositorio-de-medidas-dax-código-fuente)
    *   [7.1 Columnas Calculadas](#-71-columnas-calculadas)
    *   [7.2 Medidas Base (Totales)](#-72-medidas-base-totales)
    *   [7.3 Visual HTML: Resumen KPIs (HTML_Resumen_KPIs_V2)](#-visual-html-resumen-kpis-v2)
    *   [7.4 Visual HTML: Evolución (HTML_Evolucion_Responsive)](#-visual-html-evolución-responsive)
    *   [7.5 Visual HTML: Tarjeta NPS Animada (HTML_NPS_Card_Animated_V4_ES)](#-visual-html-tarjeta-nps-animada-v4)
    *   [7.6 Visual HTML: Tarjeta NPS Estándar (HTML_NPS_Card)](#-visual-html-tarjeta-nps-estándar)
    *   [7.7 Visual HTML: Perfil Demográfico (HTML_Perfil_Premium)](#-visual-html-perfil-demográfico)
8.  [Script Python: Generador de Datos](#-8-script-python-generador-de-datos-calibrado)
9.  [Conclusiones, Licencia y Contacto](#-9-conclusiones-licencia-y-contacto)

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

[⬆ Volver al Menú](#tabla-de-contenido-menú)

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

[⬆ Volver al Menú](#tabla-de-contenido-menú)

---

## 🧠 3. Lógica de Negocio y KPIs (DAX)

Las medidas no son simples sumas; contienen lógica de negocio para determinar el "Color del Éxito".

### 📊 Indicadores Clave (KPIs)

| Indicador | Definición | Meta / Regla de Negocio |
| :--- | :--- | :--- |
| **NPS Score** | `(Promotores % - Detractores %) * 100` | > 50 (Excelente) |
| **% Promotores** | `Total Promotores / Total Respuestas` | **Si es > 70%, se fuerza el ESTADO VERDE.** |
| **Zona de Clasificación** | Texto dinámico según el Score | Excelencia, Calidad, Mejora, Crítica. |

[⬆ Volver al Menú](#tabla-de-contenido-menú)

---

## 🎨 4. Visualización Avanzada (Frontend)

El corazón del reporte son medidas DAX complejas que renderizan HTML5 puro dentro de Power BI usando el visual "HTML Content".

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

[⬆ Volver al Menú](#tabla-de-contenido-menú)

---

## 🚦 5. Zonas de Gestión (Semáforo)

El dashboard clasifica automáticamente el desempeño del Gerente o Región en 4 zonas de actuación:

*   🏆 **Zona de Excelencia:** NPS > 75 **o** Promotores > 70%. *(Color: Verde Neón / #00E676)*.
*   ✅ **Zona de Calidad:** NPS entre 50 y 75. *(Color: Verde Medio / #00E676)*.
*   ⚠️ **Zona de Mejora:** NPS positivo pero bajo (< 50). *(Color: Amarillo-Dorado / #F4B400)*.
*   ⛔ **Zona Crítica:** NPS Negativo. *(Color: Rojo-Rosa / #E91E63)*.

[⬆ Volver al Menú](#tabla-de-contenido-menú)

---

## 📦 6. Instalación y Uso

### Pasos para desplegar:
1.  **Fuente de Datos:** Cargar el archivo generado `nps_dataset_rd_banca_claro.xlsx`.
2.  **Custom Visual:** Importar el visual **"HTML Content"** (de Daniel Marsh-Patrick) desde AppSource en Power BI.
3.  **Medidas Base:** Crear todas las medidas detalladas en la Sección 7.
4.  **Visuales Avanzados:**
    *   Seleccione el visual "HTML Content" en su lienzo.
    *   Arrastrar la medida `[HTML_NPS_Card_Animated_V4_ES]` al campo "Values" del visual para ver el velocímetro.
    *   Arrastrar la medida `[HTML_Perfil_Premium]` a otro visual HTML Content para ver la demografía.
5.  **Interacción:** Al filtrar por *Gerente*, *Año* o *Región*, ambos visuales recalculan sus vectores y colores instantáneamente.

[⬆ Volver al Menú](#tabla-de-contenido-menú)

---

## 💻 7. Repositorio de Medidas DAX (Código Fuente)

A continuación, se detalla cada medida. Siga el orden de creación para evitar errores de dependencia.

### 📌 7.1 Columnas Calculadas

#### 📝 Columna: `Rango_Edad`
*   **Propósito:** Segmentar a los clientes en grupos etarios para facilitar el análisis demográfico y la visualización en el gráfico de perfil.
*   **Lógica de Implementación:** Utiliza `SWITCH(TRUE(), ...)` para evaluar la columna numérica `[Idade]` y asignar una etiqueta de texto ("18-24", etc.).
*   **Uso en Power BI:** Crear como "Nueva Columna" en la tabla `nps_dataset_rd_banca_claro`.

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

[⬆ Volver al Menú](#tabla-de-contenido-menú)

### 📌 7.2 Medidas Base (Totales)

Estas medidas son fundamentales y sirven como base para los cálculos más complejos y los visuales HTML.

#### 📝 Medidas de Conteo y KPIs Básicos
*   **Propósito:** Calcular los volúmenes de respuestas y clasificar según la metodología NPS (Promotor: 9-10, Neutro: 7-8, Detractor: 0-6).
*   **Lógica:** Usan `CALCULATE` y `COUNTROWS` filtrando por el puntaje `[NPS_Score]`.
*   **Uso:** Crear como "Nueva Medida".

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

#### 📝 Medidas de Porcentaje y Score
*   **Propósito:** Calcular los porcentajes relativos y el Score final NPS.
*   **Lógica:** Divisiones seguras con formato.
*   **Uso:** Crear como "Nueva Medida".

```dax
Pct Promotores = 
FORMAT ( DIVIDE ( [Total Promotores], [Total Respuestas] ), "0.0%" )


Pct Neutros = 
FORMAT ( DIVIDE ( [Total Neutros], [Total Respuestas] ), "0.0%" )

Pct Detractores = 
FORMAT ( DIVIDE ( [Total Detractores], [Total Respuestas] ), "0.0%" )

NPS Zona Texto = 
VAR _NPS = [NPS Score]
RETURN
SWITCH(
    TRUE(),
    _NPS >= 70, "🏆 Excelencia",
    _NPS >= 50, "✅ Calidad",
    _NPS >= 30, "⚠️ Atención",
    _NPS >= 0,  "🟠 Mejora",
    "❌ Crítico"
)


NPS Score = 
VAR P = [Total Promotores]
VAR D = [Total Detractores]
VAR T = [Total Respuestas]
RETURN
IF (
    T = 0,
    BLANK(),
    DIVIDE ( P - D, T ) * 100
)


NPS Angulo = 
VAR _NPS = [NPS Score]
RETURN
MAX(0, MIN(180, INT(DIVIDE(_NPS + 100, 200) * 180)))
```

[⬆ Volver al Menú](#tabla-de-contenido-menú)

### 📌 Visual HTML: Resumen KPIs (HTML_Resumen_KPIs_V2)

*   **Propósito:** Generar una tarjeta compuesta tipo "Dashboard Web" que muestra todos los KPIs principales en una fila horizontal estilizada.
*   **Contexto HTML:** Construye una estructura `flexbox` con varias "tarjetas" (`div` con clase `.kpi-card`).
*   **Lógica:**
    1.  Captura los valores de las medidas base en variables (`VAR`).
    2.  Define estilos CSS internos (`<style>`) para sombras, bordes redondeados y efectos hover.
    3.  Concatena todo en un string HTML que incluye el logo (url externa) y los datos formateados.
*   **Uso:** Arrastrar esta medida a un visual "HTML Content". Asegúrese de que Power BI tenga acceso a internet para cargar el logo de Wikimedia.

```dax
HTML_Resumen_KPIs_V2 = 
-- 1. OBTENER DATOS
VAR _Total = [Total Respuestas]
VAR _Prom = [Total Promotores]
VAR _Neu  = [Total Neutros]
VAR _Det  = [Total Detractores]
VAR _PctProm = [Pct Promotores]
VAR _NPS = FORMAT([NPS Score], "0.00")

-- 2. COLORES Y ESTILOS
VAR _ColorClaro = "#DA291C" 
VAR _ColorText  = "#333333"
VAR _ColorLabel = "#888888"

RETURN
"
<style>
    /* Estilo base de cada tarjeta */
    .kpi-card {
        background: #FFFFFF;
        border-radius: 11px;       /* Reducido 2 puntos más (era 13) */
        box-shadow: 0 1px 8px rgba(0,0,0,0.06); /* Reducido 2 puntos más */
        padding: 6px 16px;         /* Reducido 2 puntos más (era 8/18) */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;       /* Centrado general */
        min-width: 136px;          /* Reducido 2 puntos más (era 138) */
        border: 1px solid #F0F0F0; 
        transition: transform 0.2s;
    }
    .kpi-card:hover {
        transform: translateY(0px); /* Ajustado */
        box-shadow: 0 4px 12px rgba(0,0,0,0.10); /* Reducido */
    }
    
    /* Título Arriba - Aumentado y Centrado */
    .kpi-title {
        font-size: 11px;           /* Aumentado 2 puntos (era 9) */
        color: #777;
        font-weight: 700;
        text-transform: uppercase;
        margin-bottom: 2px;        /* Reducido */
        letter-spacing: 0.5px;
        text-align: center;        /* Centrado */
        width: 100%;
    }

    /* Contenedor Valor + Emoji */
    .kpi-value-container {
        display: flex;
        align-items: center;
        justify-content: center;   /* Centrado */
        gap: 6px;                  /* Reducido 2 puntos más (era 8) */
    }

    /* Emoji Grande */
    .kpi-emoji {
        font-size: 24px;           /* Reducido 2 puntos más (era 26) */
    }

    /* Valor Numérico */
    .kpi-value {
        font-size: 20px;           /* Reducido 2 puntos más (era 22) */
        font-weight: 800;
        color: #333;
    }
</style>

<div style='font-family: Segoe UI, sans-serif; padding: 6px; display: flex; flex-wrap: wrap; gap: 16px; align-items: center; width: 100%; box-sizing: border-box;'>

    <div style='margin-right: 16px;'>
        <img src='https://upload.wikimedia.org/wikipedia/commons/9/99/Logo_de_Claro.svg' height='56' style='display:block;'>
    </div>

    <div class='kpi-card'>
        <div class='kpi-title'>Total Respuestas</div>
        <div class='kpi-value-container'>
            <div class='kpi-emoji'>📝</div>
            <div class='kpi-value'>" & FORMAT(_Total, "#,##0") & "</div>
        </div>
    </div>

    <div class='kpi-card' style='border-bottom: 1px solid #00E676;'> 
        <div class='kpi-title'>Promotores</div>
        <div class='kpi-value-container'>
            <div class='kpi-emoji'>😃</div>
            <div class='kpi-value'>" & FORMAT(_Prom, "#,##0") & "</div>
        </div>
    </div>

    <div class='kpi-card' style='border-bottom: 1px solid #FBC02D;'>
        <div class='kpi-title'>Neutros</div>
        <div class='kpi-value-container'>
            <div class='kpi-emoji'>😐</div>
            <div class='kpi-value'>" & FORMAT(_Neu, "#,##0") & "</div>
        </div>
    </div>

    <div class='kpi-card' style='border-bottom: 1px solid #E91E63;'>
        <div class='kpi-title'>Detractores</div>
        <div class='kpi-value-container'>
            <div class='kpi-emoji'>😡</div>
            <div class='kpi-value'>" & FORMAT(_Det, "#,##0") & "</div>
        </div>
    </div>

    <div class='kpi-card'>
        <div class='kpi-title'>% Promotores</div>
        <div class='kpi-value-container'>
            <div class='kpi-emoji'>📊</div>
            <div class='kpi-value'>" & _PctProm & "</div>
        </div>
    </div>

    <div class='kpi-card' style='background: #F9F9F9;'> 
        <div class='kpi-title' style='color: #DA291C;'>NPS Score</div>
        <div class='kpi-value-container'>
            <div class='kpi-emoji'>🚀</div>
            <div class='kpi-value' style='color: #DA291C;'>" & _NPS & "</div>
        </div>
    </div>

</div>
"
```

[⬆ Volver al Menú](#tabla-de-contenido-menú)

### 📌 Visual HTML: Evolución (HTML_Evolucion_Responsive)

*   **Propósito:** Crear un gráfico de barras comparativo (Año Actual vs Año Anterior) mes a mes usando HTML puro, sin depender de los gráficos nativos.
*   **Contexto HTML:** Genera una serie de `divs` verticales cuya altura (`height`) es un porcentaje calculado dinámicamente.
*   **Lógica:**
    1.  Genera una tabla virtual de meses (1 al 12).
    2.  Itera con `CONCATENATEX` para crear el bloque HTML de cada mes.
    3.  Calcula la altura de las barras en relación con el valor máximo del año (`_TopeEscala`), asegurando que la barra más alta sea el 100% de la altura del contenedor.
*   **Uso:** Visual "HTML Content". Ideal para headers o footers de reportes.

```dax
HTML_Evolucion_Responsive = 
-- 1. CONTEXTO DE TIEMPO
VAR _AnoActual = MAX('nps_dataset_rd_banca_claro'[Ano])
VAR _AnoAnterior = _AnoActual - 1

-- 2. GENERAMOS LOS 12 MESES (Para asegurar el eje X completo Ene-Dic)
VAR _TablaMeses = GENERATESERIES(1, 12, 1)

-- 3. CÁLCULO DEL TOPE MÁXIMO (Para escalar las barras correctamente al 100% de altura)
-- Buscamos cuál es el NPS más alto de todo el año (actual o anterior) para usarlo como techo
VAR _MaxNPS_Global = 
    MAXX(
        _TablaMeses,
        VAR _Mes = [Value]
        VAR _NPS_A = CALCULATE([NPS Score], MONTH('nps_dataset_rd_banca_claro'[Fecha]) = _Mes, 'nps_dataset_rd_banca_claro'[Ano] = _AnoActual)
        VAR _NPS_B = CALCULATE([NPS Score], MONTH('nps_dataset_rd_banca_claro'[Fecha]) = _Mes, 'nps_dataset_rd_banca_claro'[Ano] = _AnoAnterior)
        RETURN MAX(_NPS_A, _NPS_B)
    )
VAR _TopeEscala = IF(_MaxNPS_Global <= 0, 100, _MaxNPS_Global * 1.1) -- Le damos un 10% de aire arriba

-- 4. COLORES (Estilo Evolución)
VAR _ColActual = "#0F1626"   -- Azul Oscuro (Año Actual)
VAR _ColAnterior = "#90A4AE" -- Gris Azulado (Año Anterior)

VAR _FilasHTML = 
    CONCATENATEX(
        _TablaMeses,
        
        -- CÁLCULOS POR MES
        VAR _MesNum = [Value]
        VAR _MesNom = FORMAT(DATE(2023, _MesNum, 1), "MMM") -- Ene, Feb, Mar...
        
        VAR _NPS_Act = CALCULATE([NPS Score], MONTH('nps_dataset_rd_banca_claro'[Fecha]) = _MesNum, 'nps_dataset_rd_banca_claro'[Ano] = _AnoActual)
        VAR _NPS_Ant = CALCULATE([NPS Score], MONTH('nps_dataset_rd_banca_claro'[Fecha]) = _MesNum, 'nps_dataset_rd_banca_claro'[Ano] = _AnoAnterior)
        
        -- Alturas CSS (0% a 100%)
        VAR _H_Act = INT(DIVIDE(MAX(0, _NPS_Act), _TopeEscala, 0) * 100) & "%"
        VAR _H_Ant = INT(DIVIDE(MAX(0, _NPS_Ant), _TopeEscala, 0) * 100) & "%"
        
        -- Etiquetas (Evitar mostrar "0" si no hubo datos, opcional)
        VAR _Label_Act = IF(_NPS_Act = 0 && _H_Act = "0%", "", FORMAT(_NPS_Act, "0"))
        VAR _Label_Ant = IF(_NPS_Ant = 0 && _H_Ant = "0%", "", FORMAT(_NPS_Ant, "0"))
        
        RETURN
        -- SOLO DIBUJAMOS SI AL MENOS UNO DE LOS AÑOS TIENE DATOS
        IF(_NPS_Act <> 0 || _NPS_Ant <> 0,
            "<div style='display: flex; flex-direction: column; align-items: center; flex: 1; min-width: 40px;'>
                
                <!-- ÁREA DE BARRAS (Altura fija 100px) -->
                <div style='height: 120px; width: 100%; display: flex; justify-content: center; align-items: flex-end; gap: 4px; padding-bottom: 5px;'>
                    
                    <!-- BARRA ACTUAL -->
                    <div style='width: 18px; height: " & _H_Act & "; background: " & _ColActual & "; border-radius: 3px 3px 0 0; position: relative; display: flex; justify-content: center;'>
                        <span style='position: absolute; top: -14px; font-size: 10px; font-weight: 800; color: " & _ColActual & ";'>" & _Label_Act & "</span>
                    </div>
                    
                    <!-- BARRA ANTERIOR -->
                    <div style='width: 18px; height: " & _H_Ant & "; background: " & _ColAnterior & "; border-radius: 3px 3px 0 0; position: relative; display: flex; justify-content: center;'>
                        <span style='position: absolute; top: -14px; font-size: 9px; font-weight: 600; color: " & _ColAnterior & ";'>" & _Label_Ant & "</span>
                    </div>
                    
                </div>
                
                <!-- ETIQUETA MES -->
                <div style='border-top: 1px solid #EEE; width: 80%; margin-top: 2px;'></div>
                <div style='margin-top: 5px; font-size: 11px; color: #555; font-weight: 700; text-transform: uppercase;'>
                    " & _MesNom & "
                </div>
                
            </div>",
            "" -- Si no hay datos en absoluto para ese mes en ningun año, no mostrar (o cambiar a un div vacío para mantener espacio)
        ),
        
        "", 
        [Value], ASC
    )

RETURN
"
<div style='font-family: Segoe UI, sans-serif; padding: 15px; background: #fff; border-radius: 20px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); width: 100%; box-sizing: border-box;'>
    
    <!-- ENCABEZADO Y LEYENDA -->
    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid #EEE; padding-bottom: 10px;'>
        <div style='font-size: 14px; font-weight: 700; color: #555; text-transform: uppercase; letter-spacing: 1px;'>
            📅 Evolución Comparativa
        </div>
        
        <div style='display: flex; gap: 15px; font-size: 10px; font-weight: 600;'>
             <div style='display: flex; align-items: center;'>
                <div style='width: 10px; height: 10px; background: " & _ColActual & "; border-radius: 2px; margin-right: 5px;'></div>
                " & _AnoActual & "
            </div>
            <div style='display: flex; align-items: center; color: #777;'>
                <div style='width: 10px; height: 10px; background: " & _ColAnterior & "; border-radius: 2px; margin-right: 5px;'></div>
                " & _AnoAnterior & "
            </div>
        </div>
    </div>

    <!-- CONTENEDOR FLEXIBLE (RESPONSIVE) -->
    <div style='display: flex; justify-content: space-between; align-items: flex-end; width: 100%; overflow-x: auto;'>
        " & _FilasHTML & "
    </div>
    
</div>
"
```


### 📌 KPIs y Lógica de Negocio (Bloque Repetido / Referencia)

> Nota: Estas medidas ya fueron definidas en la sección 7.2. Se incluyen aquí nuevamente por completitud en caso de referencias cruzadas en el documento original.

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

[⬆ Volver al Menú](#tabla-de-contenido-menú)

### 📌 Visual HTML: Tarjeta NPS Animada (HTML_NPS_Card_Animated_V4_ES)

*   **Propósito:** Esta es la joya del reporte. Un "gauge" (velocímetro) animado con CSS que muestra el NPS Score, con "líquido" en los iconos inferiores que se llena según el porcentaje.
*   **Contexto HTML/SVG:** Utiliza SVG para dibujar los arcos del velocímetro y CSS (`transform: rotate(...)`) para mover la aguja.
*   **Lógica:**
    1.  Calcula el ángulo de la aguja (`_Angulo`) mapeando el NPS (-100 a 100) a grados (0 a 180).
    2.  Define animaciones CSS (`needle-anim`) para que la aguja se mueva suavemente al cargar.
    3.  Usa `clip-path` en SVG para crear el efecto de "llenado líquido" en los iconos de caritas inferiores.
*   **Uso:** Visual "HTML Content".

```dax
HTML_NPS_Card_Animated_V4_ES = 
-- 1. CÁLCULOS DE BASE
VAR _Total = COUNTROWS('nps_dataset_rd_banca_claro')
VAR _Prom = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Promotor")
VAR _Neu = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Neutro")
VAR _Det = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Detractor")

-- NPS Score
VAR _NPS_Raw = IF(_Total > 0, DIVIDE(_Prom - _Det, _Total) * 100, 0)

-- PORCENTAJES NUMÉRICOS
VAR _PctProm_Num = DIVIDE(_Prom, _Total, 0)
VAR _PctNeu_Num = DIVIDE(_Neu, _Total, 0)
VAR _PctDet_Num = DIVIDE(_Det, _Total, 0)

-- TEXTOS FORMATEADOS
VAR _PctProm_Txt = FORMAT(_PctProm_Num, "0%")
VAR _PctNeu_Txt = FORMAT(_PctNeu_Num, "0%")
VAR _PctDet_Txt = FORMAT(_PctDet_Num, "0%")

-- 2. COLORES DEFINITIVOS (Vibrantes)
VAR _ColDet = "#E91E63" -- Rojo/Rosa Intenso
VAR _ColNeu = "#FBC02D" -- Amarillo Oro
VAR _ColProm = "#00E676" -- Verde Neón
VAR _ColEmpty = "#E0E0E0" -- Gris para el fondo del icono (botella vacía)

-- Color Dinámico Central (Aguja y Texto)
VAR _EsTop = _PctProm_Num >= 0.70
VAR _ColorMain = 
    SWITCH(TRUE(),
        _EsTop, _ColProm,  
        _NPS_Raw >= 75, _ColProm,
        _NPS_Raw >= 50, _ColProm,
        _NPS_Raw >= 0,  _ColNeu,
        _ColDet
    )

VAR _TextoZona = 
    SWITCH(TRUE(),
        _EsTop, "Zona de Excelencia",
        _NPS_Raw >= 75, "Zona de Excelencia",
        _NPS_Raw >= 50, "Zona de Calidad",
        _NPS_Raw >= 0,  "Zona de Mejora",
        "Zona Crítica"
    )

-- 3. CÁLCULOS ANIMACIÓN
VAR _Angulo = INT(MAX(0, MIN(180, DIVIDE(_NPS_Raw + 100, 200) * 180)))

-- *** CORRECCIÓN CRÍTICA DE ESCALA SVG ***
VAR _FillY_Prom = FORMAT(24 * (1 - _PctProm_Num), "0.0", "en-US")
VAR _FillY_Neu  = FORMAT(24 * (1 - _PctNeu_Num), "0.0", "en-US")
VAR _FillY_Det  = FORMAT(24 * (1 - _PctDet_Num), "0.0", "en-US")

VAR _IconPath = "M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"

RETURN
"
<style>
    .needle-anim { transition: transform 1.5s cubic-bezier(0.34, 1.56, 0.64, 1); transform-origin: 150px 150px; }
    .liquid-anim { transition: y 1.5s ease-in-out; }
    .stat-card { transition: transform 0.2s; }
    .stat-card:hover { transform: scale(1.05); }
</style>

<div style='font-family: Segoe UI, sans-serif; background: #FFF; padding: 20px; border-radius: 30px; box-shadow: 0 15px 50px rgba(0,0,0,0.1); width: 100%; height: 100%; box-sizing: border-box; display:flex; flex-direction:column; justify-content:space-between;'>

    <div style='position: relative; height: 190px; width: 300px; margin: 0 auto;'>
        
        <div style='text-align: center; margin-bottom: 5px;'>
            <div style='color: #888; font-size: 14px; font-weight: 800; text-transform:uppercase; letter-spacing:1px;'>ZONA DE CLASIFICACIÓN (NPS)</div>
        </div>

        <svg viewBox='0 0 300 180' style='width: 100%; overflow: visible;'>
            <defs>
                <linearGradient id='gR' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='#FFCDD2'/><stop offset='1' stop-color='#E91E63'/></linearGradient>
                <linearGradient id='gY' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='#FFF9C4'/><stop offset='1' stop-color='#FBC02D'/></linearGradient>
                <linearGradient id='gG' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='#B9F6CA'/><stop offset='1' stop-color='#00E676'/></linearGradient>
            </defs>
            
            <path d='M 30 150 A 120 120 0 0 1 150 30' fill='none' stroke='" & _ColDet & "' stroke-width='22' stroke-linecap='round' stroke-dasharray='188.5 500' opacity='0.15'></path>
            <path d='M 30 150 A 120 120 0 0 1 150 30' fill='none' stroke='" & _ColDet & "' stroke-width='22' stroke-linecap='round' stroke-dasharray='188.5 500' stroke-dashoffset='0' opacity='1'></path>
            
            <path d='M 30 150 A 120 120 0 0 1 270 150' fill='none' stroke='" & _ColNeu & "' stroke-width='22' stroke-linecap='round' stroke-dasharray='94.25 500' stroke-dashoffset='-188.5' opacity='1'></path>
            
            <path d='M 30 150 A 120 120 0 0 1 270 150' fill='none' stroke='" & _ColProm & "' stroke-width='22' stroke-linecap='round' stroke-dasharray='94.25 500' stroke-dashoffset='-282.75' opacity='1'></path>

            <text x='25' y='180' font-size='14' fill='#AAA' font-weight='700'>-100</text>
            <text x='275' y='180' font-size='14' fill='#AAA' font-weight='700'>100</text>

            <g class='needle-anim' style='transform: rotate(" & _Angulo - 90 & "deg);'>
                 <circle cx='150' cy='150' r='10' fill='#333'></circle>
                 <path d='M146 150 L150 25 L154 150 Z' fill='#333'></path>
            </g>
        </svg>

        <div style='position: absolute; top: 110px; left: 50%; transform: translateX(-50%); text-align: center; 
                    background: #FFF; padding: 5px 20px; border-radius: 20px; 
                    box-shadow: 0 8px 30px rgba(0,0,0,0.15); z-index: 10;'>
            <div style='font-size: 60px; font-weight: 900; color: " & _ColorMain & "; line-height: 0.9; text-shadow: 2px 2px 0px rgba(0,0,0,0.05);'>" & FORMAT(_NPS_Raw, "0") & "</div>
            <div style='font-size: 16px; font-weight: 700; color: #555; margin-top:5px; white-space: nowrap;'>" & _TextoZona & "</div>
        </div>
    </div>

    <div style='text-align: center; margin: 15px 0 10px 0;'>
        <div style='font-size: 40px; font-weight: 800; color: #263238; letter-spacing: -1px;'>" & FORMAT(_Total, "#,##0") & "</div>
        <div style='font-size: 13px; color: #90A4AE; font-weight: 700; text-transform:uppercase;'>TOTAL DE ENCUESTAS</div>
    </div>

    <div style='display: flex; justify-content: space-between; gap: 10px;'>

        <div class='stat-card' style='flex: 1; background:#FAFAFA; border: 1px solid #EEE; border-radius:15px; padding:15px 5px; text-align: center;'>
            <div style='font-size: 24px; font-weight: 900; color: #37474F; margin-bottom: 5px;'>" & _PctDet_Txt & "</div>
            
            <div style='height: 60px; margin: 5px auto; width: 60px; position:relative;'>
                <svg width='60' height='60' viewBox='0 0 24 24'>
                    <path d='" & _IconPath & "' fill='" & _ColEmpty & "' />
                    <defs>
                        <clipPath id='clipDet'>
                            <rect x='0' y='" & _FillY_Det & "' width='24' height='24' class='liquid-anim' />
                        </clipPath>
                    </defs>
                    <path d='" & _IconPath & "' fill='" & _ColDet & "' clip-path='url(#clipDet)' />
                </svg>
            </div>
            
            <div style='font-size: 18px; font-weight: 700; color: #555;'>" & FORMAT(_Det, "#,##0") & "</div>
            <div style='font-size: 10px; color: #999; font-weight: 800; text-transform: uppercase; margin-top:2px;'>Detractores</div>
            <div style='height:4px; width:30px; background:" & _ColDet & "; margin:5px auto; border-radius:2px;'></div>
        </div>

        <div class='stat-card' style='flex: 1; background:#FAFAFA; border: 1px solid #EEE; border-radius:15px; padding:15px 5px; text-align: center;'>
            <div style='font-size: 24px; font-weight: 900; color: #37474F; margin-bottom: 5px;'>" & _PctNeu_Txt & "</div>
            
            <div style='height: 60px; margin: 5px auto; width: 60px; position:relative;'>
                <svg width='60' height='60' viewBox='0 0 24 24'>
                    <path d='" & _IconPath & "' fill='" & _ColEmpty & "' />
                    <defs><clipPath id='clipNeu'><rect x='0' y='" & _FillY_Neu & "' width='24' height='24' class='liquid-anim' /></clipPath></defs>
                    <path d='" & _IconPath & "' fill='" & _ColNeu & "' clip-path='url(#clipNeu)' />
                </svg>
            </div>
            <div style='font-size: 18px; font-weight: 700; color: #555;'>" & FORMAT(_Neu, "#,##0") & "</div>
            <div style='font-size: 10px; color: #999; font-weight: 800; text-transform: uppercase; margin-top:2px;'>Neutros</div>
            <div style='height:4px; width:30px; background:" & _ColNeu & "; margin:5px auto; border-radius:2px;'></div>
        </div>

        <div class='stat-card' style='flex: 1; background:#FAFAFA; border: 1px solid #EEE; border-radius:15px; padding:15px 5px; text-align: center;'>
            <div style='font-size: 24px; font-weight: 900; color: #37474F; margin-bottom: 5px;'>" & _PctProm_Txt & "</div>
            
            <div style='height: 60px; margin: 5px auto; width: 60px; position:relative;'>
                <svg width='60' height='60' viewBox='0 0 24 24'>
                    <path d='" & _IconPath & "' fill='" & _ColEmpty & "' />
                    <defs><clipPath id='clipProm'><rect x='0' y='" & _FillY_Prom & "' width='24' height='24' class='liquid-anim' /></clipPath></defs>
                    <path d='" & _IconPath & "' fill='" & _ColProm & "' clip-path='url(#clipProm)' />
                </svg>
            </div>
            <div style='font-size: 18px; font-weight: 700; color: #555;'>" & FORMAT(_Prom, "#,##0") & "</div>
            <div style='font-size: 10px; color: #999; font-weight: 800; text-transform: uppercase; margin-top:2px;'>Promotores</div>
            <div style='height:4px; width:30px; background:" & _ColProm & "; margin:5px auto; border-radius:2px;'></div>
        </div>

    </div>
</div>
"
```

[⬆ Volver al Menú](#tabla-de-contenido-menú)

### 📌 Visual HTML: Tarjeta NPS Estándar (HTML_NPS_Card)

*   **Propósito:** Una versión alternativa más ligera de la tarjeta NPS, sin animaciones CSS complejas, ideal si el rendimiento es una preocupación crítica.
*   **Lógica:** Similar a la anterior, pero con una estructura SVG/HTML simplificada.

```dax

HTML_NPS_Card = 
-- 1. CÁLCULOS DE BASE (Adaptados a tu tabla nps_dataset_rd_banca_claro)
VAR _Total = COUNTROWS('nps_dataset_rd_banca_claro')

VAR _Promotores = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Promotor")
VAR _Neutros = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Neutro")
VAR _Detractores = CALCULATE(COUNTROWS('nps_dataset_rd_banca_claro'), 'nps_dataset_rd_banca_claro'[Clasificacion] = "Detractor")

-- Cálculo NPS Score: ((Prom - Det) / Total) * 100
VAR _NPS_Raw = IF(_Total > 0, DIVIDE(_Promotores - _Detractores, _Total) * 100, 0)

-- 2. REGLA ESPECIAL DEL 70% PROMOTORES
VAR _PctProm_Num = DIVIDE(_Promotores, _Total, 0)
VAR _EsTopPerformance = _PctProm_Num >= 0.70

-- 3. LÓGICA DE COLOR Y TEXTO
VAR _Color = 
    SWITCH(TRUE(),
        _EsTopPerformance, "#00E676",  -- ¡FORZAR VERDE SI PROMOTORES > 70%!
        _NPS_Raw >= 75, "#00E676",
        _NPS_Raw >= 50, "#00E676",
        _NPS_Raw >= 0,  "#F4B400",
        "#E91E63"
    )

VAR _TextoZona = 
    SWITCH(TRUE(),
        _EsTopPerformance, "Zona de Excelencia", -- ¡TEXTO EXCELENCIA SI > 70%!
        _NPS_Raw >= 75, "Zona de Excelencia",
        _NPS_Raw >= 50, "Zona de Calidad",
        _NPS_Raw >= 0,  "Zona de Mejora",
        "Zona Crítica"
    )

-- 4. ÁNGULO DEL GAUGE (0 a 180 grados)
VAR _Angulo = INT(MAX(0, MIN(180, DIVIDE(_NPS_Raw + 100, 200) * 180)))

-- 5. FORMATOS DE PORCENTAJE
VAR _PctProm_Txt = FORMAT(DIVIDE(_Promotores, _Total), "0%")
VAR _PctNeu_Txt = FORMAT(DIVIDE(_Neutros, _Total), "0%")
VAR _PctDet_Txt = FORMAT(DIVIDE(_Detractores, _Total), "0%")

-- 6. ICONOS DINÁMICOS POR SEXO
VAR _SexoSel = SELECTEDVALUE('nps_dataset_rd_banca_claro'[Sexo], "Todos")
VAR _IconPath = 
    SWITCH(_SexoSel,
        "Femenino", "M12,4A2,2 0 0,1 14,6C14,7.1 13.1,8 12,8A2,2 0 0,1 10,6C10,4.9 10.9,4 12,4M17,12V10H7V12H9V21H11V14H13V21H15V12H17Z", -- Icono Mujer
        "Masculino", "M9,14H15V21H13V16H11V21H9V14M12,12C14.21,12 16,10.21 16,8C16,5.79 14.21,4 12,4C9.79,4 8,5.79 8,8C8,10.21 9.79,12 12,12M18,14V10H6V14H8V24H16V14H18Z", -- Icono Hombre
        "M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z" -- Icono Default (Grupo)
    )

RETURN
"
<div style='font-family: Segoe UI, sans-serif; background: white; padding: 20px; border-radius: 25px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); width: 100%; height: 100%; box-sizing: border-box; position: relative;'>

    <div style='display: flex; justify-content: center; align-items: center; margin-bottom: 5px;'>
        <div style='text-align: center;'>
            <div style='color: #333; font-size: 16px; font-weight: 600; text-transform: uppercase;'>ZONA DE CLASIFICACIÓN (NPS)</div>
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
        <div style='font-size: 14px; color: #7f8c8d; font-weight: 600; text-transform: uppercase;'>TOTAL DE ENCUESTAS</div>
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
            <div style='font-size: 11px; color: #777; font-weight: 600;'>Detractores</div>
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

[⬆ Volver al Menú](#tabla-de-contenido-menú)

### 📌 Visual HTML: Perfil Demográfico (HTML_Perfil_Premium)

*   **Propósito:** Mostrar la distribución demográfica (Edad y Sexo) en una sola tarjeta combinada y elegante.
*   **Lógica:**
    1.  Calcula los totales por rango de edad (18-29, 30-39, etc.) y sexo.
    2.  Determina el valor máximo para escalar las barras de progreso (`width: %`).
    3.  Construye un HTML Grid donde cada fila es un rango de edad, con barras bicolores.
*   **Uso:** Visual "HTML Content".

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

#### 📌 Variante / Backup: HTML_Perfil_Premium (Versión Alternativa)
> Esta versión alternativa aparece en el registro original. Se recomienda usar la versión principal documentada arriba.

```dax
HTML_Perfil_Premium - = 
VAR _Total = COUNTROWS(nps_dataset_rd_banca_claro)
VAR _Masc = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Sexo] = "Masculino") + 0
VAR _Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0

-- Porcentajes de texto
VAR _PctMascTxt = FORMAT(DIVIDE(_Masc, _Total), "0%")
VAR _PctFemTxt = FORMAT(DIVIDE(_Fem, _Total), "0%")

VAR _ColorMasc = "#0F1626"
VAR _ColorFem = "#E91E63"

-- CÁLCULOS DE GRUPOS (USANDO LA COLUMNA NUMÉRICA 'Idade' DIRECTAMENTE)
-- Rango 1: 18 a 29
VAR _R1_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 18, nps_dataset_rd_banca_claro[Idade] <= 29) + 0
VAR _R1_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 18, nps_dataset_rd_banca_claro[Idade] <= 29, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R1_Masc = _R1_Tot - _R1_Fem

-- Rango 2: 30 a 39
VAR _R2_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 30, nps_dataset_rd_banca_claro[Idade] <= 39) + 0
VAR _R2_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 30, nps_dataset_rd_banca_claro[Idade] <= 39, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R2_Masc = _R2_Tot - _R2_Fem

-- Rango 3: 40 a 49
VAR _R3_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 40, nps_dataset_rd_banca_claro[Idade] <= 49) + 0
VAR _R3_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 40, nps_dataset_rd_banca_claro[Idade] <= 49, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R3_Masc = _R3_Tot - _R3_Fem

-- Rango 4: 50 a 59
VAR _R4_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 50, nps_dataset_rd_banca_claro[Idade] <= 59) + 0
VAR _R4_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 50, nps_dataset_rd_banca_claro[Idade] <= 59, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R4_Masc = _R4_Tot - _R4_Fem

-- Rango 5: 60+ (acima 59)
VAR _R5_Tot = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 60) + 0
VAR _R5_Fem = CALCULATE(COUNTROWS(nps_dataset_rd_banca_claro), nps_dataset_rd_banca_claro[Idade] >= 60, nps_dataset_rd_banca_claro[Sexo] = "Femenino") + 0
VAR _R5_Masc = _R5_Tot - _R5_Fem

-- ESCALA MÁXIMA (DENOMINADOR)
VAR _MaxVal = MAXX({_R1_Tot, _R2_Tot, _R3_Tot, _R4_Tot, _R5_Tot}, [Value])
VAR _Denom = IF(_MaxVal = 0, 1, _MaxVal) * 1.2

-- CÁLCULO DE ANCHOS (width) CON 'INT'
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
            <svg width='50' height='50' viewBox='0 0 24 24'>
                <path d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z' fill='" & _ColorMasc & "'/>
            </svg>
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

        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>18 a 29</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R1_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R1_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R1_Tot & "</div>
        </div>

        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>30 a 39</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R2_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R2_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R2_Tot & "</div>
        </div>

        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>40 a 49</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R3_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R3_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R3_Tot & "</div>
        </div>

        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 45px; text-align: right; font-size: 11px; color: #666; margin-right: 8px;'>50 a 59</div>
            <div style='flex: 1; display: flex; background: #f0f0f0; border-radius: 4px; overflow: hidden;'>
                <div style='height: 22px; width: " & _W_R4_F & "%; background: " & _ColorFem & ";'></div>
                <div style='height: 22px; width: " & _W_R4_M & "%; background: " & _ColorMasc & ";'></div>
            </div>
            <div style='width: 30px; margin-left: 8px; font-weight: bold; color: #333; font-size: 11px;'>" & _R4_Tot & "</div>
        </div>

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

[⬆ Volver al Menú](#tabla-de-contenido-menú)

---

## 🐍 8. Script Python: Generador de Datos Calibrado

Utiliza este script para generar el archivo `nps_dataset_rd_banca_claro.xlsx`. El script asegura que los datos reflejen una tendencia positiva ("Winner Logic") para alinearse con la narrativa del dashboard.

### Instrucciones de Ejecución:
1.  Asegúrese de tener Python instalado.
2.  Instale las librerías necesarias: `pip install pandas numpy openpyxl`.
3.  Guarde el siguiente código en un archivo llamado `generar_datos.py`.
4.  Ejecute el script. El archivo Excel se generará en la misma carpeta.

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

[⬆ Volver al Menú](#tabla-de-contenido-menú)

---

## 9. Conclusiones y Contacto

### Conclusiones
Este proyecto demuestra cómo superar las limitaciones nativas de Power BI combinando lógica de negocio avanzada con tecnologías web (HTML/CSS/SVG). El resultado es un dashboard ejecutivo de alto impacto, interactivo y alineado con los estándares de diseño modernos.

### Licencia
Este manual y el código fuente asociado son para uso educativo y demostrativo.

### Contacto
Si tiene dudas sobre la implementación de las medidas DAX o el uso de visuales HTML, consulte la documentación oficial de Power BI o contacte al desarrollador del proyecto.

[⬆ Volver al Menú](#tabla-de-contenido-menú)
