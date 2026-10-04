#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Efectral DSL — Validador y Linter Normativo (efc-validator)
Proyecto: Efectral Agents AI — E J G 4
Autor: Julio César Gallardo
Licencia: MIT
"""

import sys
import os
import re
import argparse
from typing import List, Tuple, Dict, Any

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

VALID_DIRECTIVE_VERBS = {"Identifícate", "Aplica", "Fija", "Prohíbe"}
VALID_ACTION_VERBS = {"Verifica", "Extrae", "Escribe", "Ejecuta", "Emite", "EsperaInstrucciones"}

class ValidationError:
    def __init__(self, line_num: int, col_num: int, rule_id: str, message: str, line_content: str):
        self.line_num = line_num
        self.col_num = col_num
        self.rule_id = rule_id
        self.message = message
        self.line_content = line_content.strip()

    def __str__(self):
        return f"  L{self.line_num}:{self.col_num} [{self.rule_id}] {self.message}\n    Línea: {self.line_content}"


class EfectralValidator:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.errors: List[ValidationError] = []
        self.stats = {
            "lines": 0,
            "blocks": 0,
            "directives": 0,
            "actions": 0,
            "variables": 0
        }

    def validate(self) -> bool:
        if not os.path.exists(self.filepath):
            self.errors.append(ValidationError(0, 0, "FILE-01", f"Archivo no encontrado: {self.filepath}", ""))
            return False

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                content = f.read()
        except UnicodeDecodeError as e:
            self.errors.append(ValidationError(1, 1, "UTF8-01", f"El archivo no es UTF-8 válido: {e}", ""))
            return False
        except Exception as e:
            self.errors.append(ValidationError(0, 0, "IO-01", f"Error de lectura: {e}", ""))
            return False

        lines = content.splitlines()
        self.stats["lines"] = len(lines)

        self._check_bracket_balance(content)
        self._analyze_lines(lines)

        return len(self.errors) == 0

    def _check_bracket_balance(self, content: str):
        """Verifica que todos los corchetes y paréntesis estén equilibrados respetando bloques del parser."""
        stack: List[Tuple[str, int, int]] = []
        in_string = False
        escape = False
        in_parser_block = False

        for line_num, raw_line in enumerate(content.splitlines(), start=1):
            stripped_line = raw_line.strip()
            if in_parser_block:
                if stripped_line == "#Fin":
                    in_parser_block = False
                continue
            elif stripped_line.startswith("#") and stripped_line != "#Fin":
                in_parser_block = True
                continue

            col_num = 0
            line_len = len(raw_line)
            
            # Detectar y saltar ordinal inicial tipo "1) " o "  12) "
            ordinal_match = re.match(r"^(\s*[0-9]+)\)", raw_line)
            start_col = 0
            if ordinal_match:
                start_col = len(ordinal_match.group(0))

            i = start_col
            while i < line_len:
                ch = raw_line[i]
                col_num = i + 1

                if escape:
                    escape = False
                    i += 1
                    continue

                if ch == '\\':
                    escape = True
                    i += 1
                    continue

                if ch == '"':
                    in_string = not in_string
                    i += 1
                    continue

                if in_string:
                    i += 1
                    continue

                # Comprobación de corchetes y paréntesis
                if ch in ('[', '('):
                    stack.append((ch, line_num, col_num))
                elif ch in (']', ')'):
                    expected = '[' if ch == ']' else '('
                    if not stack:
                        self.errors.append(ValidationError(
                            line_num, col_num, "DELIM-01",
                            f"Delimitador de cierre '{ch}' sin apertura correspondiente.",
                            raw_line
                        ))
                    else:
                        last_open, o_line, o_col = stack.pop()
                        if last_open != expected:
                            self.errors.append(ValidationError(
                                line_num, col_num, "DELIM-02",
                                f"Desajuste de delimitadores: se esperaba el cierre de '{last_open}' (de L{o_line}:{o_col}) pero se encontró '{ch}'.",
                                raw_line
                            ))
                i += 1

        if in_string:
            self.errors.append(ValidationError(
                line_num, col_num, "STRING-01",
                "Cadena de texto con comillas sin cerrar al final del archivo.",
                ""
            ))

        for unclosed, u_line, u_col in stack:
            self.errors.append(ValidationError(
                u_line, u_col, "DELIM-03",
                f"Delimitador '{unclosed}' nunca fue cerrado.",
                f"Abierto en L{u_line}:{u_col}"
            ))

    def _analyze_lines(self, lines: List[str]):
        """Analiza línea por línea la conformidad con la especificación 1.0.0."""
        in_block = False
        block_depth = 0
        in_parser_block = False

        for idx, line in enumerate(lines, start=1):
            stripped = line.strip()

            if not stripped:
                continue

            if in_parser_block:
                if stripped == "#Fin":
                    in_parser_block = False
                continue
            elif stripped.startswith("#") and stripped != "#Fin":
                in_parser_block = True
                continue

            # Detect block opening: Identificador:[
            block_open_match = re.match(r"^([A-Za-zÁ-Úá-úÑñ0-9_]+):\[(.*)$", stripped)
            if block_open_match:
                self.stats["blocks"] += 1
                in_block = True
                block_depth += 1
                remainder = block_open_match.group(2).strip()
                if remainder.endswith("]"):
                    block_depth -= 1
                    if block_depth == 0:
                        in_block = False
                continue

            if stripped == "]":
                if block_depth > 0:
                    block_depth -= 1
                    if block_depth == 0:
                        in_block = False
                continue

            # Directives starting with @
            if "@" in stripped:
                directive_matches = re.finditer(r"@([A-Za-zÁ-Úá-úÑñ0-9_]+)\b", stripped)
                for dm in directive_matches:
                    verb = dm.group(1)
                    self.stats["directives"] += 1

            # Action instructions starting with !
            if "!" in stripped:
                action_matches = re.finditer(r"!([A-Za-zÁ-Úá-úÑñ0-9_]+)\b", stripped)
                for am in action_matches:
                    verb = am.group(1)
                    self.stats["actions"] += 1

            # Variables tracking
            var_matches = re.findall(r"\$([A-Za-zÁ-Úá-úÑñ0-9_]+)", stripped)
            if var_matches:
                self.stats["variables"] += len(var_matches)

            # Verificación de la Regla de No-Prosa
            if not in_block:
                if not stripped.startswith("@") and not stripped.startswith("!"):
                    if not re.match(r"^[0-9]+\)\s*!", stripped) and not stripped.startswith("["):
                        self.errors.append(ValidationError(
                            idx, 1, "RULE-01",
                            "Violación de la Regla de No-Prosa: Contenido suelto fuera de bloques estructurados.",
                            line
                        ))
            else:
                # Análisis Morfosintáctico: Verificar Ley de Verbos Atómicos
                if "!" in stripped:
                    invalid_verbs = re.findall(r"!([a-z]+[A-Z][a-zA-Z]*|[A-Z][a-z]+[A-Z][a-zA-Z]*)", stripped)
                    if invalid_verbs:
                        self.errors.append(ValidationError(
                            idx, 1, "MORPH-01",
                            f"Violación de Ley del Sujeto Tácito: Los verbos deben ser atómicos. PascalCase/CamelCase prohibido: !{invalid_verbs[0]}",
                            line
                        ))

                    # Análisis de Módulos / Tentáculos
                    invoca_match = re.search(r"!Invoca\(\s*Tentaculo\s*:\s*\[(.*?)\]\s*\)", stripped)
                    if invoca_match:
                        tentaculo_file = invoca_match.group(1).strip()
                        # TODO: Asegurar la ruta base exacta si el contexto de ejecución varía
                        # Por defecto busca en un subdirectorio 'tentacles/' relativo al directorio del archivo
                        base_dir = os.path.dirname(os.path.abspath(self.filepath))
                        tentacle_path = os.path.join(base_dir, "tentacles", tentaculo_file)
                        if not os.path.exists(tentacle_path):
                            self.errors.append(ValidationError(
                                idx, 1, "MOD-01",
                                f"Tentáculo no encontrado: El archivo '{tentaculo_file}' no existe en el directorio físico 'tentacles/'.",
                                line
                            ))

                # Dentro de un bloque estructurado, solo se admiten elementos normativos
                es_directiva = stripped.startswith("@")
                es_accion = bool(re.match(r"^([0-9]+\)\s*)?!", stripped))
                es_declaracion = bool(re.match(r"^-?[A-Za-zÁ-Úá-úÑñ0-9_]+:\s*(\[|\"|[A-Za-zÁ-Úá-ú0-9_]+)", stripped)) or bool(re.match(r"^-?[A-Za-zÁ-Úá-úÑñ0-9_]+:", stripped))
                es_bifurcacion = bool(re.match(r"^\[.+\]\s*(->|entonces|y|o)\b", stripped)) or bool(re.match(r"^(si\s*no\s*entonces|entonces)\b", stripped))
                es_sifalla = bool(re.match(r"^SiFalla(:\s*\[|\s+entonces)?", stripped))
                es_herramienta = bool(re.match(r"^(Herramienta|Subagente)\s*\(", stripped))
                es_cierre = stripped == "]" or stripped.endswith("]")

                if not (es_directiva or es_accion or es_declaracion or es_bifurcacion or es_sifalla or es_herramienta or es_cierre):
                    self.errors.append(ValidationError(
                        idx, 1, "RULE-01",
                        "Violación de la Regla de No-Prosa: Frase o texto libre no estructurado dentro del bloque.",
                        line
                    ))


def validate_path(path: str, verbose: bool = False) -> Tuple[int, int]:
    """Valida un archivo o todos los archivos .efd en un directorio."""
    target_files = []
    if os.path.isfile(path):
        target_files.append(path)
    elif os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                if file.endswith(".efd"):
                    target_files.append(os.path.join(root, file))
    else:
        print(f"Error: Ruta '{path}' no válida.")
        return 0, 1

    total_valid = 0
    total_invalid = 0

    print("=" * 68)
    print("  Efectral DSL — VALIDADOR Y LINTER NORMATIVO (EFC)")
    print("  E J G 4 — Julio César Gallardo")
    print("=" * 68)

    for fpath in target_files:
        validator = EfectralValidator(fpath)
        is_valid = validator.validate()

        try:
            rel_path = os.path.relpath(fpath)
        except ValueError:
            rel_path = fpath
        if is_valid:
            total_valid += 1
            st = validator.stats
            print(f"[OK] {rel_path} (L:{st['lines']} | Bloques:{st['blocks']} | @:{st['directives']} | !:{st['actions']} | $:{st['variables']})")
        else:
            total_invalid += 1
            print(f"[FALLA] {rel_path} ({len(validator.errors)} error(es) encontrados):")
            for err in validator.errors:
                print(err)
            print()

    print("-" * 68)
    print(f"Resumen: {total_valid} archivo(s) conformes, {total_invalid} archivo(s) con errores.")
    print("=" * 68)

    return total_valid, total_invalid


def main():
    parser = argparse.ArgumentParser(
        description="Validador y Linter oficial para archivos Efectral DSL (.efd) conforme a la especificación 1.0.0."
    )
    parser.add_argument("path", nargs="?", default=".", help="Archivo .efd o directorio a validar (por defecto: directorio actual)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo detallado")

    args = parser.parse_args()
    _, invalid = validate_path(args.path, args.verbose)

    sys.exit(0 if invalid == 0 else 1)


if __name__ == "__main__":
    main()
