"""\
TOPSTSCHOOL Sphinx Configuration
===============================

Author: Akshay Mestry <xa@mes3.dev>
Created on: Saturday, August 17 2024
Last updated on: Friday, August 30 2024

This file contains the configuration settings for building the TOPSTSCHOOL
documentation using Sphinx, a popular Python documentation tool. Sphinx
is a powerful documentation generator that makes it easy to create high
quality technical documentation for technical projects.

This configuration file is used to specify the Sphinx documentation
build process. It tells Sphinx where to find the source files for the
documentation, what output format to generate, and other options that
control how the documentation is built.

Usage::

    To use this configuration file, copy it to the root directory of
    Sphinx project, in this case the `osdmp` directory and customize
    the settings as needed. You can then run the Sphinx build process by
    running the command:

        `sphinx-build -EWaq -b html source/ build/`
"""

from __future__ import annotations

import typing as t
from datetime import datetime as dt

# -- General configurations ---------------------------------------------------
extensions: list[str] = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
]
exclude_patterns: list[str] = []
templates_path: list[str] = ["_templates"]

# -- Miscellaneous ------------------------------------------------------------
nitpicky: bool = True
source: t.Final[str] = "https://github.com/ciesin-geospatial/TOPSTSCHOOL-OSDMP"
baseurl: t.Final[str] = "https://ciesin-geospatial.github.io"
intersphinx_mapping: dict[str, tuple[str, t.Any]] = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
rst_epilog = ""
with open("_static/urls.txt") as f:
    rst_epilog += f.read()

# -- Project information -----------------------------------------------------
html_coeus_author: t.Final[str] = "TOPSTSCHOOL Development Team"
html_coeus_copyright: t.Final[str] = f"{dt.now().year}, {html_coeus_author}."
html_coeus_email: t.Final[str] = "TOPSTSCHOOL@gmail.com"
html_coeus_github: str = source + "/docs"
html_coeus_include_last_updated_date: bool = True
html_coeus_license: str = f"{source}/blob/main/LICENSE"
html_coeus_repository: str = source
html_coeus_title: t.Final[str] = "TOPSTSCHOOL"
html_coeus_version: t.Final[str] = "2024.08.30"
html_coeus_favicon: t.Final[str] = "_static/img/favicon.png"
html_coeus_logo: t.Final[str] = "_static/img/logo.png"
html_coeus_hide_index_toctree: bool = True
html_coeus_homepage: str = f"{baseurl}/TOPSTSCHOOL/"
html_coeus_documentation: str = html_coeus_homepage
html_coeus_theme_options: dict[str, t.Any] = {
    "show_previous_next_pages": True,
}

# -- Options for HTML output --------------------------------------------------
html_theme: t.Final[str] = "coeus_sphinx_theme"
html_static_path: list[str] = ["_static"]
html_css_files: list[str] = ["css/override.css"]
tags_badge_colors: dict[str, str] = {"article": "success"}
