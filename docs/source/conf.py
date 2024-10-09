"""\
TOPSTSCHOOL Sphinx Configuration
===============================

Author: Akshay Mestry <xa@mes3.dev>
Created on: Saturday, August 17 2024
Last updated on: Wednesday, October 09 2024

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

import glob
import os
import shutil
import subprocess
import typing as t
from datetime import datetime as dt

from jupyterlite_sphinx import jupyterlite_sphinx
from sphinx.application import Sphinx

# -- General configurations ---------------------------------------------------
extensions: list[str] = [
    "jupyterlite_sphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]
exclude_patterns: list[str] = [
    ".DS_Store",
    "Thumbs.db",
    "_build",
]
templates_path: list[str] = ["_templates"]

# -- Miscellaneous ------------------------------------------------------------
nitpicky: bool = True
source: t.Final[str] = "https://github.com/ciesin-geospatial/TOPSTSCHOOL-OSDMP"
baseurl: t.Final[str] = "https://ciesin-geospatial.github.io"
intersphinx_mapping: dict[str, tuple[str, t.Any]] = {
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "xarray": ("https://docs.xarray.dev/en/stable/", None),
    "ipython": ("https://ipython.readthedocs.io/en/stable/", None),
}

rst_epilog = ""
with open("_static/urls.txt") as f:
    rst_epilog += f.read()

try:
    last_updated_cmd = (
        "git",
        "log",
        "--pretty=format:%cd",
        "--date=format:%B %d, %Y",
        "-n1",
    )
    last_updated = subprocess.check_output(last_updated_cmd).decode()
except Exception:
    last_updated = None

# -- Project information -----------------------------------------------------
html_coeus_author: t.Final[str] = "TOPST SCHOOL Development Team"
html_coeus_copyright: t.Final[str] = f"{dt.now().year}, {html_coeus_author}."
html_coeus_email: t.Final[str] = "TOPSTSCHOOL@gmail.com"
html_coeus_github: str = source
html_coeus_license: str = f"{source}/blob/main/LICENSE"
html_coeus_repository: str = source
html_coeus_title: t.Final[str] = "TOPST SCHOOL Universe"
html_coeus_version: t.Final[str] = "2024.10.31"
html_coeus_favicon: t.Final[str] = "_static/img/favicon.png"
html_coeus_logo: t.Final[str] = "_static/img/logo.png"
html_coeus_hide_index_toctree: bool = True
html_coeus_homepage: str = f"{baseurl}/TOPSTSCHOOL-OSDMP/"
html_coeus_documentation: str = html_coeus_homepage
html_coeus_theme_options: dict[str, t.Any] = {
    "last_updated": last_updated,
    "show_previous_next_pages": True,
    "supported_languages": {"en": "English", "es": "Español"},
    "navbar_links": {
        "Open Science Resources": {
            "External Resources": "_resources/external-resources",
            "Glossary": "_resources/glossary",
        },
        "Community": {
            "Contribution Guidelines": "_community/contributor-guidelines",
            "Events & Webinars": "_community/upcoming-events",
            "Review & Approval": "_community/becoming-reviewer",
            "Meet the Team": "_community/meet-the-team",
        },
        "About Us": {
            "Vision & Mission": "_about-us/vision-mission",
            "How to Get Involved": "_about-us/getting-involved",
            "Announcements": "_about-us/announcements",
        },
    },
}
locale_dirs: list[str] = ["../locale/"]
gettext_compact: bool = False

# -- Options for HTML output --------------------------------------------------
html_theme: t.Final[str] = "coeus_sphinx_theme"
html_static_path: list[str] = ["_static"]
html_css_files: list[str] = ["css/override.css"]
html_context: dict[str, str] = {"feedback_link": source + ("/discussions/44")}

# -- Options for Jupyter Notebook Embedding -----------------------------------
jupyterlite_bind_ipynb_suffix: bool = False
jupyterlite_silence: bool = True
jupyterlite_dir: str = "_jupyter"


def topst_jupyterlite_build(app: Sphinx, error: t.Any) -> None:
    """Monkey-patched Jupyterlite build."""
    if error is not None:
        return

    if app.builder.format == "html":
        jupyterlite_config = app.env.config.jupyterlite_config
        jupyterlite_contents = app.env.config.jupyterlite_contents
        jupyterlite_dir = str(app.env.config.jupyterlite_dir)
        jupyterlite_build_command_options: dict[str, t.Any] = (
            app.env.config.jupyterlite_build_command_options
        )
        config = []
        if jupyterlite_config:
            config = ["--config", jupyterlite_config]
        if jupyterlite_contents is None:
            jupyterlite_contents = []
        elif isinstance(jupyterlite_contents, str):
            jupyterlite_contents = [jupyterlite_contents]
        jupyterlite_contents = [
            match
            for pattern in jupyterlite_contents
            for match in glob.glob(pattern, recursive=True)
        ]
        contents = []
        for content in jupyterlite_contents:
            contents.extend(["--contents", content])
        apps_option = []
        for liteapp in [
            "notebooks",
            "edit",
            "lab",
            "repl",
            "tree",
            "consoles",
        ]:
            apps_option.extend(["--apps", liteapp])
        voici = None
        if voici is not None:
            apps_option.extend(["--apps", "voici"])
        lite_dir = os.path.join(app.srcdir, jupyterlite_dir)
        if not os.path.exists(lite_dir):
            os.makedirs(lite_dir, exist_ok=True)
        command = [
            "jupyter",
            "lite",
            "build",
            "--debug",
            *config,
            *contents,
            "--contents",
            os.path.join(lite_dir, "content"),
            "--output-dir",
            os.path.join(app.outdir, jupyterlite_dir),
            *apps_option,
            "--lite-dir",
            lite_dir,
        ]
        if jupyterlite_build_command_options is not None:
            for key, value in jupyterlite_build_command_options.items():
                if key in ["contents", "output-dir", "lite-dir"]:
                    raise RuntimeError("These options are not supported")
                command.extend([f"--{key}", str(value)])
        assert all(
            [isinstance(s, str) for s in command]
        ), f"Expected all commands arguments to be a str, got {command}"
        kwargs: dict[str, t.Any] = {}
        if app.env.config.jupyterlite_silence:
            kwargs["stdout"] = subprocess.PIPE
            kwargs["stderr"] = subprocess.PIPE
        completed_process: subprocess.CompletedProcess[bytes] = subprocess.run(
            command, cwd=app.srcdir, check=True, **kwargs
        )
        if completed_process.returncode != 0:
            if app.env.config.jupyterlite_silence:
                print(
                    "Command `jupyterlite build` failed but its output has "
                    "been silenced. stdout and stderr are reproduced below.\n"
                )
                print("stdout:", completed_process.stdout.decode())
                print("stderr:", completed_process.stderr.decode())
            raise subprocess.CalledProcessError(
                returncode=completed_process.returncode,
                cmd=command,
                output=completed_process.stdout,
                stderr=completed_process.stderr,
            )
    try:
        shutil.rmtree(os.path.join(app.srcdir, "_contents"))
        os.remove(os.path.join(app.srcdir, ".jupyterlite.doit.db"))
    except FileNotFoundError:
        pass


jupyterlite_sphinx.jupyterlite_build = topst_jupyterlite_build
