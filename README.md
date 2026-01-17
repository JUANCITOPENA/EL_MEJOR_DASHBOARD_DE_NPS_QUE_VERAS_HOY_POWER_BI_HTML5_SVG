# 🦁 Dashboard Ejecutivo NPS: Banca & Telecomunicaciones (Premium UI)

> **Versión:** 2.0 (High Performance Edition)  
> **Tecnología:** Power BI + DAX + HTML5/SVG + Python  
> **Enfoque:** Visualización de Datos Avanzada (Custom Visuals via DAX)

---

## 📖 1. Narrativa y Contexto del Negocio

### 🏦 El Escenario
"Banca Claro RD" es una institución líder que busca monitorear la satisfacción de sus clientes (NPS) en tiempo real. La alta dirección requiere un tablero que no solo muestre números, sino que **transmita el éxito y la excelencia** de la gestión actual.

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

* **Periodo:** 3 años de histórico.
* **Cobertura:** Nacional (Regiones Ozama, Cibao, Sur, Este).
* **Segmentación:** Sexo, Rango de Edad (calculado dinámicamente), Plan, Gerente.
* **Calibración Positiva (The "Winner" Logic):**
    * 🟩 **Promotores (9-10):** ~78% (Mayoría absoluta).
    * 🟨 **Neutros (7-8):** ~8% (Minimizado).
    * 🟥 **Detractores (0-6):** ~14% (Controlado).

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

El corazón del reporte son dos medidas DAX complejas que renderizan HTML5 puro dentro de Power BI.

### 1️⃣ Tarjeta NPS (Velocímetro SVG)
Un componente visual complejo diseñado a medida que incluye:

* **Gauge Semicircular (SVG):** Dibuja un arco de 180° dinámico y nítido.
* **Aguja Rotatoria:** Calcula el ángulo exacto basado en el NPS (Escala de -100 a 100).
    * *Fórmula de rotación:* `INT(MAX(0, MIN(180, (_NPS + 100) * 0.9)))`
* **Indicadores de Segmento:** Barras de progreso inferiores con iconos vectoriales (SVG path) que cambian de color según el segmento.
* **Clean UI:** Se eliminaron botones innecesarios (como el botón "Edit") para ofrecer una vista ejecutiva limpia y centrada en el dato.

### 2️⃣ Tarjeta Perfil del Cliente (Demografía)
Un panel informativo que desglosa quién está respondiendo la encuesta:

* **Iconos de Género:** Vectores SVG que cambian dinámicamente según el sexo predominante en la selección.
* **Barras Apiladas (CSS Grid):**
    * Muestra la distribución de edad (18-29, 30-39, etc.).
    * Utiliza barras bicolores (Rosa/Azul Oscuro) dentro del mismo contenedor visual.
* **Técnica Web:** Uso de `width: %` en divs HTML calculados via DAX para la longitud de las barras.
* **Corrección de Error:** Se usa la columna numérica `[Idade]` para calcular los rangos "al vuelo" dentro de la medida, evitando errores de texto o conflictos con columnas calculadas previas.

---

## 🚦 5. Zonas de Gestión (Semáforo)

El dashboard clasifica automáticamente el desempeño del Gerente o Región en 4 zonas de actuación:

* 🏆 **Zona de Excelencia:** NPS > 75 **o** Promotores > 70%. *(Color: Verde Neón / #00E676)*.
* ✅ **Zona de Calidad:** NPS entre 50 y 75. *(Color: Verde Medio / #00E676)*.
* ⚠️ **Zona de Mejora:** NPS positivo pero bajo (< 50). *(Color: Amarillo-Dorado / #F4B400)*.
* ⛔ **Zona Crítica:** NPS Negativo. *(Color: Rojo-Rosa / #E91E63)*.

---

## 📦 6. Instalación y Uso

### Pasos para desplegar:
1.  **Fuente de Datos:** Cargar el archivo generado `nps_dataset_rd_banca_claro.xlsx`.
2.  **Custom Visual:** Importar el visual **"HTML Content"** (de Daniel Marsh-Patrick) desde AppSource.
3.  **Medidas:**
    * Arrastrar la medida `[HTML_NPS_Card]` al lienzo para ver el velocímetro.
    * Arrastrar la medida `[HTML_Perfil_Premium]` al lienzo para ver la demografía.
4.  **Interacción:** Al filtrar por *Gerente*, *Año* o *Región*, ambos visuales recalculan sus vectores y colores instantáneamente.

> **Nota del Desarrollador:** Este dashboard demuestra que Power BI no tiene límites visuales si se combina correctamente con lenguajes web (HTML/CSS).
