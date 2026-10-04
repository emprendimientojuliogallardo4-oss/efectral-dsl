# Registro de Cambios (Changelog) - Efectral DSL

Todas las actualizaciones notables de la Arquitectura Efectral DSL se documentarÃ¡n en este archivo.
El formato sigue el estÃ¡ndar de registro histÃ³rico para facilitar la lectura de agentes y humanos.

---

## [2.0.0] - El Hard Fork: Morfosintaxis Agéntica y Arquitectura Modular Efectral OS - (Versión Actual)

### 🚀 Cambio (Qué cambió y Cómo)
- **Evolución a Morfosintaxis Agéntica:** El DSL dejó de ser solo una plantilla estructural para convertirse en un *Instruction Set Architecture (ISA)* estricto. Se adoptó la Ley del Sujeto Tácito: los OpCodes ahora son Verbos Transitivos Atómicos en imperativo activo (ej. !Invoca, !Extrae). Prohibido el uso de PascalCase/CamelCase en los verbos.
- **Operadores Lógicos Nativos:** Integración oficial de conectores en español puro (y, o, entonces, si no) reemplazando los operadores simbólicos (&&, ||) para fluidificar el razonamiento neuronal.
- **Redefinición del Parser (#META):** El símbolo # fue despojado de su uso como "comentario visual" y ahora es estrictamente reservado para los bloques que el motor host lee invisiblemente (#META ... #Fin).
- **Arquitectura de Módulos y Tentáculos:** Abandono oficial de las Skills en Markdown monolítico (paradigma OpenClaw). El DSL ahora orquesta un ecosistema modular de 3 capas: efc_env.yaml (ADN/Dependencias), 	entacles/ (Código Puro), y CORE.efd (Cerebro Lógico).
- **Linter Físico (efc_validator.py):** El analizador morfosintáctico fue actualizado para interceptar el OpCode !Invoca(Tentaculo:[X]) y verificar físicamente la existencia del script en el disco duro del módulo.
- **Reset de Branding:** Erradicación oficial de las nomenclaturas "Efectral 4". El sistema es un único Sistema Operativo Agéntico Soberano: **Efectral**.

### 🧠 Motivo (Por qué y Resultado)
- **¿Por qué?** El paradigma anterior dependía de prosa en Markdown y cargaba miles de tokens de scripts Bash y Python en el contexto de la IA. Era el "Síndrome del Agente Obeso".
- **Resultado:** Al separar el código físico en *Tentáculos* y dejar solo la lógica morfosintáctica en el archivo .efd, la ejecución se volvió matemáticamente determinista. Efectral ahora opera como el Kernel de un Sistema Operativo (Efectral OS).

---

## [1.2.0] - Discriminador de Tipo y Regla de Herencia OntolÃ³gica - (VersiÃ³n Actual)

### ðŸš€ Cambio (QuÃ© cambiÃ³ y CÃ³mo)
- **Discriminador de Tipo en `BloqueIdentidad`:** EvoluciÃ³n del esquema canÃ³nico de identificaciÃ³n de `@IdentifÃ­cate(Agente:[X])` a `@IdentifÃ­cate(Tipo:[T], Nombre:[X])`.
- **Vocabulario Cerrado de Tipos:** Se define formalmente el conjunto cerrado de identificadores ontolÃ³gicos para `Tipo`: `{Agente, Skill, Configuracion, Herramienta, Bloque, Memoria}`.
- **Regla de Herencia OntolÃ³gica:** Los metadatos de gobernanza global (`-Organizacion`), la directiva de transparencia (`@Aplica(Regla:[Transparencia])`) y las reglas base del sistema viven **exclusivamente** en el artefacto raÃ­z de tipo `[Agente]`. Los artefactos secundarios (`Skill`, `Configuracion`, `Herramienta`, `Bloque`, `Memoria`) heredan la autoridad ontolÃ³gica raÃ­z y no duplican estos campos, declarando Ãºnicamente `Tipo` + `Nombre` + `Rol` + `Mision` y sus especificaciones tÃ©cnicas locales.
- **ActualizaciÃ³n de Plantillas y Ejemplos:** EstandarizaciÃ³n de `library/bloque_identidad.efd`, la cÃ©dula raÃ­z `efectral-native-v1/IDENTITY.efd`, y la totalidad de los ejemplos canÃ³nicos en `examples/*.efd` y `core/examples/*.efd`.
- **EvoluciÃ³n Documental:** ActualizaciÃ³n normativa en `SPECIFICATION.md` (secciones 3.1, 4.5 y 4.6), `library/GLOSSARY.md` y delimitaciÃ³n en `docs/SINTAXIS_SEMANTICA_FLEXIBLE.md`.

### ðŸ§  Motivo (Por quÃ© y Resultado)
- **Â¿Por quÃ©?** En sistemas agÃ©nticos modulares avanzados (principio Kernel Linux), los submÃ³dulos auxiliares no deben tratarse ontolÃ³gicamente como agentes raÃ­z ni saturar la ventana de contexto repitiendo declaraciones organizacionales o de transparencia. Se requerÃ­a una distinciÃ³n formal e inequÃ­voca de la naturaleza de cada artefacto sin perder el determinismo estructural.
- **Resultado:** JerarquÃ­a limpia, atÃ³mica y altamente escalable. Los LLMs y validadores identifican instantÃ¡neamente el rol del archivo en la arquitectura global, preservando la ventana de atenciÃ³n al eliminar redundancias de gobernanza en componentes subordinados.

### ðŸ“ Archivos Afectados
- `VERSION`
- `CHANGELOG.md`
- `SPECIFICATION.md`
- `library/GLOSSARY.md`
- `library/bloque_identidad.efd`
- `docs/SINTAXIS_SEMANTICA_FLEXIBLE.md`
- `efectral-native-v1/IDENTITY.efd`
- `examples/01_hello_agent.efd`
- `examples/02_safe_guardrails.efd`
- `examples/03_pipeline_data.efd`
- `examples/04_efectral_4_canonical.efd`
- `examples/05_agente_funcional_en_blanco.efd`
- `examples/06_agente_contenido.efd`
- `core/examples/01_hello_agent.efd`
- `core/examples/02_safe_guardrails.efd`
- `core/examples/03_pipeline_data.efd`
- `core/examples/04_efectral_4_canonical.efd`
- `core/examples/05_agente_funcional_en_blanco.efd`

---

## [1.1.0] - EvoluciÃ³n SemÃ¡ntica y EstandarizaciÃ³n

### ðŸš€ AÃ±adido (QuÃ© cambiÃ³ y CÃ³mo)
- **Sintaxis SemÃ¡ntica Flexible:** Se integrÃ³ el documento `docs/SINTAXIS_SEMANTICA_FLEXIBLE.md` que establece la inmunidad al idioma y la capacidad de la IA para inventar etiquetas deterministas en tiempo real (ej. `!Ruta`, `!ModulaTono`).
- **Traductor Universal NLP a DSL:** CreaciÃ³n de `directives/NL_TO_DSL_PROMPT.md`. Un metaprompt estandarizado para inyectar en cualquier LLM, ordenÃ¡ndole actuar como Arquitecto Efectral.
- **Sistema de Versionado:** CreaciÃ³n del archivo raÃ­z `VERSION` y `docs/VERSIONADO.md` para anclar el estado del proyecto.

### ðŸ§  PropÃ³sito (Por quÃ© y Resultado)
- **Â¿Por quÃ©?** Porque el repositorio pÃºblico necesitaba ser 100% modular y reproducible. Los usuarios e IAs externas estaban limitados a "copiar" plantillas rÃ­gidas en lugar de "programar" lÃ³gicas fluidas basadas en el lenguaje natural.
- **Resultado:** Efectral DSL ya no es solo una plantilla, es un *Lenguaje de ProgramaciÃ³n AgÃ©ntica DinÃ¡mico*. Cualquier IA puede leer el metaprompt y generar capas cognitivas masivas y personalizadas sin romper el estÃ¡ndar.

---

## [1.0.0] - GÃ©nesis (Clean Slate)

### ðŸš€ AÃ±adido
- **Lanzamiento de Efectral Native v1:** Despliegue oficial de la arquitectura.
- **Reinicio HistÃ³rico (Clean Slate):** EliminaciÃ³n total del historial de Git anterior para establecer una base pura y auditable.
- **Purga de Vestigios:** ErradicaciÃ³n de las dependencias y terminologÃ­a heredada de las versiones no oficiales (Efectral 4).
- **Estructura Base:** ConsolidaciÃ³n de los bloques fundamentales (`BloqueIdentidad`, `BloqueReglas`, `BloqueEjecucion`) y el glosario central.

