# EFECTRAL DSL

<div align="center">

**El Meta-Lenguaje Formal, Tipado y Determinista para la Inteligencia Artificial**

[![VersiÃ³n](https://img.shields.io/badge/versiÃ³n-2.0.0--estable-blue.svg)](#)
[![Licencia](https://img.shields.io/badge/licencia-MIT-green.svg)](./LICENSE)
[![OrganizaciÃ³n](https://img.shields.io/badge/organizaciÃ³n-E%20J%20G%204-purple.svg)](#)
[![ValidaciÃ³n EFC](https://img.shields.io/badge/validador%20efc-conforme-brightgreen.svg)](#)

*"Programar la mente de la IA con morfosintaxis pura, no sugerirle en prosa."*

</div>

---

## 0. DeclaraciÃ³n Soberana y PosiciÃ³n de DiseÃ±o

> [!IMPORTANT]
> **EVOLUCIÃ“N DEL LENGUAJE (v2.0.0):**  
> Efectral DSL ha evolucionado hacia la **Morfosintaxis AgÃ©ntica**. Este repositorio contiene exclusivamente las reglas gramaticales, la especificaciÃ³n y los validadores de este lenguaje.  
> 
> La arquitectura del lenguaje opera bajo:
> - **Ley del Sujeto TÃ¡cito:** Las acciones se declaran matemÃ¡ticamente mediante Verbos Transitivos AtÃ³micos (`!Invoca`, `!Verifica`, `!Extrae`).
> - **Cero Prosa:** Se prohÃ­ben las instrucciones en lenguaje natural.
> - **Conectores LÃ³gicos Nativos:** Reemplazo de sintaxis matemÃ¡tica compleja por lÃ³gica fluida determinista (`y`, `o`, `entonces`, `si no`).

---

## 1. DefiniciÃ³n OntolÃ³gica: Â¿QuÃ© es Efectral DSL?

1. **La GramÃ¡tica del Razonamiento:**
   - Efectral DSL (`.efd`) es un lenguaje de diseÃ±o creado para estructurar rÃ­gidamente la forma en que un LLM razona y decide.
2. **Determinismo LingÃ¼Ã­stico:**
   - Evita la ambigÃ¼edad del Markdown tradicional. Al obligar al modelo a parsear Bloques (`#META...#Fin`) y directivas (`@`, `!`), se elimina la alucinaciÃ³n operativa.
3. **Uso de la LibrerÃ­a Central (`/library`):**
   - El estÃ¡ndar exige la composiciÃ³n mediante bloques canÃ³nicos: `BloqueIdentidad`, `BloqueReglas`, `BloqueSeguridad`, `BloqueEjecucion`.

---

## 2. Herramientas del Ecosistema

- **Validador EFC (`tools/efc_validator.py`):** Linter estricto que parsea archivos `.efd` para asegurar el cumplimiento de la Morfosintaxis AgÃ©ntica, validando la estructura de verbos, conectores lÃ³gicos y el uso exclusivo de los bloques `#META`.

---

## 3. Licencia y AutorÃ­a

* **OrganizaciÃ³n:** [E J G 4](https://github.com/emprendimientojuliogallardo4-oss)
* **Arquitecto y Creador:** Julio CÃ©sar Gallardo
* **Licencia:** MIT License. Libre para uso, integraciÃ³n, modificaciÃ³n y despliegue comercial o de investigaciÃ³n.

