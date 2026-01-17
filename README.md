# 📊 Panel de Control NPS Interactivo (Web Edition)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)
![Status](https://img.shields.io/badge/status-stable-success)
![Technology](https://img.shields.io/badge/tech-HTML5%20%7C%20CSS3%20%7C%20JS-orange)

> **Una experiencia visual intuitiva y de alto rendimiento para el análisis de NPS (Net Promoter Score), desarrollada desde cero con tecnologías web estándar.**

---

## 📑 Tabla de Contenidos

1. [📖 Introducción](#-introducción)
2. [✨ Características Principales](#-características-principales)
3. [🛠️ Tecnologías Utilizadas](#-tecnologías-utilizadas)
4. [📋 Prerrequisitos](#-prerrequisitos)
5. [🚀 Instalación y Despliegue](#-instalación-y-despliegue)
6. [💻 Estructura del Proyecto](#-estructura-del-proyecto)
7. [🎨 Diseño y UX](#-diseño-y-ux)
8. [🤝 Contribución](#-contribución)
9. [👏 Créditos y Agradecimientos](#-créditos-y-agradecimientos)
10. [📄 Licencia](#-licencia)

---

## 📖 Introducción

Este proyecto nace con la misión de transformar datos fríos en una narrativa visual atractiva. A diferencia de los paneles tradicionales limitados por software de BI (Business Intelligence), esta solución es una **Web App Standalone** que ofrece libertad total en diseño y performance.

El objetivo fue replicar y superar la experiencia de un dashboard ejecutivo, implementando lógicas de **ETL (simulado en JS)** y visualización de datos avanzada utilizando únicamente estándares web modernos.

---

## ✨ Características Principales

*   **⚡ Alto Rendimiento:** Carga instantánea y transiciones fluidas sin la sobrecarga de motores de BI pesados.
*   **🏎️ Infografía de Velocímetro:** Visualización SVG dinámica que reacciona a los KPIs del NPS en tiempo real.
*   **🗺️ Mapa Interactivo:** Gráficos vectoriales que permiten el desglose geográfico de la satisfacción del cliente.
*   **👤 Perfil de Cliente Dinámico:** Tooltips y descripciones personalizadas que cambian según la selección de datos.
*   **🎨 Background Figma-Designed:** Una interfaz de usuario pulida con fondos y activos exportados directamente desde diseños de alta fidelidad.

---

## 🛠️ Tecnologías Utilizadas

Este proyecto no utiliza frameworks pesados, garantizando la máxima compatibilidad y facilidad de replicación.

| Tecnología | Rol | Icono |
| :--- | :--- | :--- |
| **HTML5** | Estructura semántica y accesibilidad | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" width="20" height="20"/> |
| **CSS3** | Estilos, Grid/Flexbox y Animaciones | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" width="20" height="20"/> |
| **JavaScript (ES6+)** | Lógica de negocio, manipulación del DOM y cálculos de NPS | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" width="20" height="20"/> |
| **Figma** | Prototipado y diseño de assets gráficos | <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/figma/figma-original.svg" width="20" height="20"/> |
| **SVG** | Gráficos vectoriales escalables para métricas nítidas | 📐 |

---

## 📋 Prerrequisitos

Para ejecutar o editar este proyecto, necesitas:

1.  **Navegador Web Moderno:** Chrome, Edge, Firefox o Safari (versiones recientes).
2.  **Editor de Código (Opcional):** Se recomienda [Visual Studio Code](https://code.visualstudio.com/) para explorar el código.
3.  **Git (Opcional):** Para clonar el repositorio.

---

## 🚀 Instalación y Despliegue

Sigue estos pasos para tener el proyecto corriendo en tu máquina local en menos de 2 minutos.

### Paso 1: Clonar u Obtener el Proyecto

Si tienes Git instalado, abre tu terminal y ejecuta:

```bash
git clone https://github.com/tu-usuario/nps-dashboard-web.git
cd nps-dashboard-web
```

*Si descargaste el archivo ZIP, simplemente extrae el contenido en una carpeta de tu preferencia.*

### Paso 2: Ejecución

Al ser un proyecto estático (Client-Side), no requieres instalar Node.js ni configurar servidores complejos.

**Opción A (Doble Clic):**
1.  Navega a la carpeta del proyecto.
2.  Haz doble clic en el archivo `index.html`.
3.  El dashboard se abrirá en tu navegador predeterminado.

**Opción B (VS Code Live Server - Recomendado):**
1.  Abre la carpeta en VS Code.
2.  Instala la extensión "Live Server".
3.  Haz clic derecho en `index.html` y selecciona **"Open with Live Server"**.

---

## 💻 Estructura del Proyecto

La organización de archivos sigue las mejores prácticas para facilitar el mantenimiento:

```text
nps-dashboard/
│
├── 📂 assets/              # Recursos estáticos
│   ├── 📂 images/          # Fondos de Figma e iconos rasterizados
│   └── 📂 svgs/            # Gráficos vectoriales (Velocímetro, Mapa)
│
├── 📂 css/                 # Hojas de estilo
│   ├── style.css           # Estilos principales y reset
│   └── responsive.css      # Media queries para adaptabilidad
│
├── 📂 js/                  # Lógica del cliente
│   ├── data.js             # Datos simulados (JSON structure)
│   ├── main.js             # Lógica principal de renderizado
│   └── charts.js           # Lógica específica para gráficos SVG
│
├── index.html              # Punto de entrada de la aplicación
├── README.md               # Documentación del proyecto
└── LICENSE                 # Licencia de uso
```

---

## 🎨 Diseño y UX

El diseño visual fue concebido en **Figma** antes de escribir una sola línea de código.

1.  **Fondo y Contenedores:** Se exportaron como SVGs/PNGs para mantener la fidelidad visual.
2.  **Interactividad:**
    *   *Hover Effects:* Al pasar el mouse sobre las regiones del mapa.
    *   *Data Binding:* Al hacer clic en un segmento del velocímetro, la información del perfil del cliente se actualiza automáticamente.

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Si deseas mejorar el código o añadir nuevas visualizaciones:

1.  Haz un **Fork** del proyecto.
2.  Crea una nueva rama (`git checkout -b feature/NuevaFuncionalidad`).
3.  Realiza tus cambios y haz **Commit** (`git commit -m 'Agrega nueva gráfica'`).
4.  Haz **Push** a la rama (`git push origin feature/NuevaFuncionalidad`).
5.  Abre un **Pull Request**.

---

## 👏 Créditos y Agradecimientos

Este proyecto fue posible gracias a la inspiración y conocimientos técnicos adquiridos.

*   **Autor:** [Tu Nombre / Usuario]
*   **Mentoría:** Un agradecimiento especial al **Profesor Jefferson Alves** por sus enseñanzas en visualización de datos y diseño de dashboards, que sirvieron de base conceptual para esta implementación web.

---

## 📄 Licencia

Este proyecto está bajo la Licencia **MIT**. Eres libre de usarlo, modificarlo y distribuirlo, siempre y cuando se mantenga la atribución al autor original.

```text
MIT License
Copyright (c) 2026 [Tu Nombre]
```

---
*Documentación generada automáticamente con estándares de ingeniería de software.*
