#!/usr/bin/env python3
"""
Root Build Script for GKM Elektrik Engineering Hub
Executes markdown generation and static site compilation.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GEN_DIR = os.path.join(BASE_DIR, "generator")
sys.path.append(GEN_DIR)

import content_builder
import engine

if __name__ == "__main__":
    print("[BUILD] Generating content and compiling static pages...")
    content_builder.build_markdown_files()
    engine.compile_site()
    print("[BUILD] Build complete! Static assets are ready in dist/")
