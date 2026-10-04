#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Efectral DSL — Instalador Autónomo de Entorno de Desarrollo (IDE)
Instala la extensión oficial de Efectral DSL (.efd) en Antigravity IDE, VS Code y Cursor.
Proyecto: Efectral Agents AI — E J G 4
Autor: Julio César Gallardo
Licencia: MIT
"""

import sys
import os
import shutil

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

EXTENSION_NAME = "efectral-dsl-support-1.0.0"

def get_target_directories():
    """Detecta las carpetas de extensiones instaladas en la máquina del usuario."""
    home = os.path.expanduser("~")
    candidates = [
        ("VS Code", os.path.join(home, ".vscode", "extensions")),
        ("Cursor", os.path.join(home, ".cursor", "extensions")),
        ("Antigravity IDE", os.path.join(home, ".antigravity-ide", "extensions")),
        ("Antigravity App", os.path.join(home, ".gemini", "antigravity", "extensions")),
    ]
    return candidates

def install():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    package_json = os.path.join(repo_root, "package.json")
    syntaxes_dir = os.path.join(repo_root, "syntaxes")
    snippets_dir = os.path.join(repo_root, "snippets")
    lang_config = os.path.join(repo_root, "language-configuration.json")

    if not os.path.exists(package_json):
        print(f"Error: No se encontró package.json en {repo_root}")
        sys.exit(1)

    print("=" * 68)
    print("  Efectral DSL — INSTALADOR AUTÓNOMO DE EXTENSIÓN DE IDE")
    print("  E J G 4 — Julio César Gallardo")
    print("=" * 68)

    installed_count = 0
    targets = get_target_directories()

    for name, base_path in targets:
        dest_folder = os.path.join(base_path, EXTENSION_NAME)
        try:
            # Crear la carpeta base de extensiones si existe el directorio padre
            parent = os.path.dirname(base_path)
            if not os.path.exists(parent):
                continue

            os.makedirs(dest_folder, exist_ok=True)

            # Copiar manifiesto y configuraciones
            shutil.copy2(package_json, os.path.join(dest_folder, "package.json"))
            if os.path.exists(lang_config):
                shutil.copy2(lang_config, os.path.join(dest_folder, "language-configuration.json"))
            readme_path = os.path.join(repo_root, "README.md")
            if os.path.exists(readme_path):
                shutil.copy2(readme_path, os.path.join(dest_folder, "README.md"))
            license_path = os.path.join(repo_root, "LICENSE")
            if os.path.exists(license_path):
                shutil.copy2(license_path, os.path.join(dest_folder, "LICENSE"))

            # Copiar syntaxes
            dest_syntaxes = os.path.join(dest_folder, "syntaxes")
            os.makedirs(dest_syntaxes, exist_ok=True)
            for f in os.listdir(syntaxes_dir):
                shutil.copy2(os.path.join(syntaxes_dir, f), os.path.join(dest_syntaxes, f))

            # Copiar snippets
            if os.path.exists(snippets_dir):
                dest_snippets = os.path.join(dest_folder, "snippets")
                os.makedirs(dest_snippets, exist_ok=True)
                for f in os.listdir(snippets_dir):
                    shutil.copy2(os.path.join(snippets_dir, f), os.path.join(dest_snippets, f))

            print(f"[INSTALADO] {name} -> {dest_folder}")
            installed_count += 1
        except Exception as e:
            print(f"[OMITIDO] {name}: {e}")

    print("-" * 68)
    if installed_count > 0:
        print(f"¡Éxito! Entorno de Efectral DSL instalado en {installed_count} editor(es).")
        print("Reinicia tu editor (VS Code, Cursor o Antigravity IDE) para activar el soporte.")
    else:
        # Si no encontró ninguna de las carpetas estándar, instalar al menos en .vscode por defecto
        fallback = os.path.join(os.path.expanduser("~"), ".vscode", "extensions", EXTENSION_NAME)
        try:
            os.makedirs(fallback, exist_ok=True)
            shutil.copy2(package_json, os.path.join(fallback, "package.json"))
            if os.path.exists(lang_config):
                shutil.copy2(lang_config, os.path.join(fallback, "language-configuration.json"))
            dest_syntaxes = os.path.join(fallback, "syntaxes")
            os.makedirs(dest_syntaxes, exist_ok=True)
            for f in os.listdir(syntaxes_dir):
                shutil.copy2(os.path.join(syntaxes_dir, f), os.path.join(dest_syntaxes, f))
            if os.path.exists(snippets_dir):
                dest_snippets = os.path.join(fallback, "snippets")
                os.makedirs(dest_snippets, exist_ok=True)
                for f in os.listdir(snippets_dir):
                    shutil.copy2(os.path.join(snippets_dir, f), os.path.join(dest_snippets, f))
            print(f"[INSTALADO POR DEFECTO] -> {fallback}")
            print("Reinicia tu editor para activar el soporte.")
        except Exception as e:
            print(f"Error en instalación por defecto: {e}")
    print("=" * 68)

if __name__ == "__main__":
    install()
