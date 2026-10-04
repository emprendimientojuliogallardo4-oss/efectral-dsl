#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Efectral DSL — Generador de Paquete VSIX Oficial
Empaqueta la extensión para distribución universal en VS Code, Cursor y Antigravity IDE.
E J G 4 — Julio César Gallardo
"""

import os
import sys
import zipfile

def build_vsix():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    dist_dir = os.path.join(repo_root, "dist")
    os.makedirs(dist_dir, exist_ok=True)
    
    vsix_path = os.path.join(dist_dir, "efectral-dsl-support-1.0.0.vsix")

    content_types_xml = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="application/json" />
  <Default Extension="vsixmanifest" ContentType="text/xml" />
  <Default Extension="md" ContentType="text/markdown" />
  <Default Extension="txt" ContentType="text/plain" />
</Types>
"""

    vsix_manifest_xml = """<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Id="efectral-dsl-support" Version="1.0.0" Language="en-US" Publisher="EJG4" />
    <DisplayName>Efectral DSL Language Support</DisplayName>
    <Description xml:space="preserve">Soporte oficial de sintaxis y lenguaje para Efectral DSL (.efd) en VS Code, Cursor y Antigravity.</Description>
    <Tags>efectral,efd,dsl,ai-agents,prompt-engineering,determinism</Tags>
    <Categories>Programming Languages</Categories>
    <GalleryFlags>Public</GalleryFlags>
    <Properties>
      <Property Id="Microsoft.VisualStudio.Code.Engine" Value="^1.74.0" />
      <Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value="" />
    </Properties>
    <License>extension/LICENSE</License>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code" />
  </Installation>
  <Dependencies />
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.Details" Path="extension/README.md" Addressable="true" />
    <Asset Type="Microsoft.VisualStudio.Services.Content.License" Path="extension/LICENSE" Addressable="true" />
  </Assets>
</PackageManifest>
"""

    files_to_pack = [
        ("package.json", "extension/package.json"),
        ("language-configuration.json", "extension/language-configuration.json"),
        ("syntaxes/efectral.tmLanguage.json", "extension/syntaxes/efectral.tmLanguage.json"),
        ("snippets/efectral.json", "extension/snippets/efectral.json"),
        ("README.md", "extension/README.md"),
        ("LICENSE", "extension/LICENSE"),
    ]

    print(f"Empaquetando extensión VSIX oficial en {vsix_path}...")
    with zipfile.ZipFile(vsix_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types_xml.strip())
        zf.writestr("extension.vsixmanifest", vsix_manifest_xml.strip())

        for src_rel, dest_zip_path in files_to_pack:
            src_full = os.path.join(repo_root, src_rel)
            if not os.path.exists(src_full):
                # Fallback a ide-extension/
                ide_candidate = os.path.join(repo_root, "ide-extension", src_rel)
                if os.path.exists(ide_candidate):
                    src_full = ide_candidate
            if os.path.exists(src_full):
                zf.write(src_full, dest_zip_path)
            else:
                print(f"[AVISO] Archivo no encontrado para empaquetar: {src_full}")

    size_kb = os.path.getsize(vsix_path) / 1024
    print(f"[VSIX GENERADO] {vsix_path} ({size_kb:.2f} KB)")
    return vsix_path

if __name__ == "__main__":
    build_vsix()
