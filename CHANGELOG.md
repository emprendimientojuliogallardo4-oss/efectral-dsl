# Registro de Cambios (Changelog) - Efectral DSL

Todas las actualizaciones notables de la Arquitectura Efectral DSL se documentarán en este archivo.
El formato sigue el estándar de registro histórico para facilitar la lectura de agentes y humanos.

---

## [2.0.0] - Evolución a Morfosintaxis Agéntica - (Versión Actual)

### 🚀 Cambio (Qué cambió y Cómo)
- **Morfosintaxis Agéntica:** El DSL dejó de ser solo una plantilla estructural para convertirse en un lenguaje estricto y tipado. Se adoptó la Ley del Sujeto Tácito: los OpCodes ahora son Verbos Transitivos Atómicos en imperativo activo (ej. `!Invoca`, `!Extrae`). Prohibido el uso de PascalCase/CamelCase interno en los verbos.
- **Operadores Lógicos Nativos:** Integración oficial de conectores lingüísticos (`y`, `o`, `entonces`, `si no`) reemplazando los operadores simbólicos heredados (`&&`, `||`) para fluidificar el razonamiento neuronal.
- **Redefinición del Parser (#META):** El símbolo `#` fue despojado de su uso como "comentario visual" y ahora es estrictamente reservado para los bloques de código máquina (`#META ... #Fin`).
- **Validador Morfosintáctico (`efc_validator.py`):** El linter fue reescrito para interpretar de forma estricta los nuevos operadores lógicos y rechazar cualquier instrucción que viole la atomicidad de los verbos o contenga prosa.

### 🧠 Motivo (Por qué y Resultado)
- **¿Por qué?** El paradigma anterior aún permitía descripciones conversacionales que diluían la atención del modelo.
- **Resultado:** Efectral DSL ahora es puramente determinista. Obliga a la Inteligencia Artificial a operar como un procesador lógico absoluto, erradicando la alucinación por ambigüedad.

---

## [1.2.0] - Discriminador de Tipo y Regla de Herencia Ontológica

### 🚀 Cambio (Qué cambió y Cómo)
- **Discriminador de Tipo en `BloqueIdentidad`:** Evolución del esquema canónico de identificación de `@Identifícate(Agente:[X])` a `@Identifícate(Tipo:[T], Nombre:[X])`.
- **Vocabulario Cerrado de Tipos:** Se define formalmente el conjunto cerrado de identificadores ontológicos para `Tipo`: `{Agente, Skill, Configuracion, Herramienta, Bloque, Memoria}`.
- **Regla de Herencia Ontológica:** Los metadatos de gobernanza global (`-Organizacion`), la directiva de transparencia (`@Aplica(Regla:[Transparencia])`) y las reglas base del sistema viven **exclusivamente** en el artefacto raíz de tipo `[Agente]`. Los artefactos secundarios (`Skill`, `Configuracion`, `Herramienta`, `Bloque`, `Memoria`) heredan la autoridad ontológica raíz y no duplican estos campos, declarando únicamente `Tipo` + `Nombre` + `Rol` + `Mision` y sus especificaciones técnicas locales.
- **Actualización de Plantillas y Ejemplos:** Estandarización de `library/bloque_identidad.efd`, la cédula raíz `efectral-native-v1/IDENTITY.efd`, y la totalidad de los ejemplos canónicos en `examples/*.efd` y `core/examples/*.efd`.
- **Evolución Documental:** Actualización normativa en `SPECIFICATION.md` (secciones 3.1, 4.5 y 4.6), `library/GLOSSARY.md` y delimitación en `docs/SINTAXIS_SEMANTICA_FLEXIBLE.md`.

### 🧠 Motivo (Por qué y Resultado)
- **¿Por qué?** En sistemas agénticos modulares avanzados (principio Kernel Linux), los submódulos auxiliares no deben tratarse ontológicamente como agentes raíz ni saturar la ventana de contexto repitiendo declaraciones organizacionales o de transparencia. Se requería una distinción formal e inequívoca de la naturaleza de cada artefacto sin perder el determinismo estructural.
- **Resultado:** Jerarquía limpia, atómica y altamente escalable. Los LLMs y validadores identifican instantáneamente el rol del archivo en la arquitectura global, preservando la ventana de atención al eliminar redundancias de gobernanza en componentes subordinados.

---

## [1.1.0] - Evolución Semántica y Estandarización

### 🚀 Añadido (Qué cambió y Cómo)
- **Sintaxis Semántica Flexible:** Se integró el documento `docs/SINTAXIS_SEMANTICA_FLEXIBLE.md` que establece la inmunidad al idioma y la capacidad de la IA para inventar etiquetas deterministas en tiempo real (ej. `!Ruta`, `!ModulaTono`).
- **Traductor Universal NLP a DSL:** Creación de `directives/NL_TO_DSL_PROMPT.md`. Un metaprompt estandarizado para inyectar en cualquier LLM, ordenándole actuar como Arquitecto Efectral.
- **Sistema de Versionado:** Creación del archivo raíz `VERSION` y `docs/VERSIONADO.md` para anclar el estado del proyecto.

### 🧠 Propósito (Por qué y Resultado)
- **¿Por qué?** Porque el repositorio público necesitaba ser 100% modular y reproducible. Los usuarios e IAs externas estaban limitados a "copiar" plantillas rígidas en lugar de "programar" lógicas fluidas basadas en el lenguaje natural.
- **Resultado:** Efectral DSL ya no es solo una plantilla, es un *Lenguaje de Programación Agéntica Dinámico*. Cualquier IA puede leer el metaprompt y generar capas cognitivas masivas y personalizadas sin romper el estándar.

---

## [1.0.0] - Génesis (Clean Slate)

### 🚀 Añadido
- **Lanzamiento de Efectral Native v1:** Despliegue oficial de la arquitectura.
- **Reinicio Histórico (Clean Slate):** Eliminación total del historial de Git anterior para establecer una base pura y auditable.
- **Purga de Vestigios:** Erradicación de las dependencias y terminología heredada de las versiones no oficiales (Efectral 4).
- **Estructura Base:** Consolidación de los bloques fundamentales (`BloqueIdentidad`, `BloqueReglas`, `BloqueEjecucion`) y el glosario central.
