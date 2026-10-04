# EFECTRAL DSL (v2.0.0)

<div align="center">

**El Meta-Lenguaje Formal, Tipado y Determinista para la Inteligencia Artificial**

[![Versión](https://img.shields.io/badge/versión-2.0.0--estable-blue.svg)](#)
[![Licencia](https://img.shields.io/badge/licencia-MIT-green.svg)](./LICENSE)
[![Organización](https://img.shields.io/badge/organización-E%20J%20G%204-purple.svg)](#)
[![Validación EFC](https://img.shields.io/badge/validador%20efc-conforme-brightgreen.svg)](#)

*"Programar la mente de la IA con morfosintaxis pura, no sugerirle en prosa."*

</div>

---

## 0. Declaración Soberana y Posición de Diseño

> [!IMPORTANT]
> **EVOLUCIÓN DEL LENGUAJE (v2.0.0):**  
> Efectral DSL ha evolucionado hacia la **Morfosintaxis Agéntica**. Este repositorio contiene exclusivamente las reglas gramaticales, la especificación y los validadores de este lenguaje.  
> 
> La arquitectura del lenguaje opera bajo:
> - **Ley del Sujeto Tácito:** Las acciones se declaran matemáticamente mediante Verbos Transitivos Atómicos (`!Invoca`, `!Verifica`, `!Extrae`).
> - **Cero Prosa:** Se prohíben las instrucciones en lenguaje natural.
> - **Conectores Lógicos Nativos:** Reemplazo de sintaxis matemática compleja por lógica fluida determinista (`y`, `o`, `entonces`, `si no`).

---

## 1. Definición Ontológica: ¿Qué es Efectral DSL?

1. **La Gramática del Razonamiento:**
   - Efectral DSL (`.efd`) es un lenguaje de diseño creado para estructurar rígidamente la forma en que un LLM razona y decide.
2. **Determinismo Lingüístico:**
   - Evita la ambigüedad del Markdown tradicional. Al obligar al modelo a parsear Bloques (`#META...#Fin`) y directivas (`@`, `!`), se elimina la alucinación operativa.
3. **Uso de la Librería Central (`/library`):**
   - El estándar exige la composición mediante bloques canónicos: `BloqueIdentidad`, `BloqueReglas`, `BloqueSeguridad`, `BloqueEjecucion`.

---

## 2. Herramientas del Ecosistema

- **Validador EFC (`tools/efc_validator.py`):** Linter estricto que parsea archivos `.efd` para asegurar el cumplimiento de la Morfosintaxis Agéntica, validando la estructura de verbos, conectores lógicos y el uso exclusivo de los bloques `#META`.

---

## 3. Licencia y Autoría

* **Organización:** [E J G 4](https://github.com/emprendimientojuliogallardo4-oss)
* **Arquitecto y Creador:** Julio César Gallardo
* **Licencia:** MIT License. Libre para uso, integración, modificación y despliegue comercial o de investigación.
