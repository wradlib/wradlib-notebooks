#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (c) 2025, wradlib developers.
# Distributed under the MIT License. See LICENSE-MIT for more info.

import os
import sys

import pyproj
import wradlib

# set PROJ_LIB explicitly to overcome RTD issue
os.environ["PROJ_LIB"] = pyproj.datadir.get_data_dir()
os.environ["PROJ_NETWORK"] = "ON"

sys.path.insert(0, os.path.abspath(".."))

project = "wradlib notebooks"
copyright = "2025, wradlib developers"
author = "Kai Mühlbauer"

wradlib_version = wradlib.__version__
html_title = " ".join([project, wradlib_version])


extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # "sphinxcontrib.bibtex",
    "myst_nb",
    "sphinx_copybutton",
    "IPython.sphinxext.ipython_console_highlighting",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
    "html_image",
    "linkify",
    "substitution",
    "tasklist",
    "replacements",
]

autosectionlabel_prefix_document = True

myst_heading_anchors = 4

source_suffix = {
    ".rst": "restructuredtext",
    ".ipynb": "notebook",
}

myst_nb = {"kernelspec": {"name": "python3", "display_name": "Python 3"}}

myst_substitutions = {
    "wradlib": "$\\omega radlib$",
    "wradlib_version": wradlib_version,
}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/", None),
    "matplotlib": ("https://matplotlib.org/stable/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "xarray": ("https://docs.xarray.dev/en/stable/", None),
    "xradar": ("https://docs.openradarscience.org/projects/xradar/en/stable/", None),
    "cartopy": ("https://cartopy.readthedocs.io/stable/", None),
    "gdal": ("https://gdal.org/en/stable/", None),
    "pyproj": ("https://pyproj4.github.io/pyproj/stable/", None),
    "wradlib": ("https://docs.wradlib.org/en/stable/", None),
}


master_doc = "index"

html_theme = "sphinx_book_theme"

html_theme_options = {
    "show_toc_level": 1,
    "collapse_navigation": True,
    "extra_footer": f"<div>Created with wradlib v{wradlib_version}</div>",
}

nb_execution_mode = "force"
nb_execution_kernel_name = "python3"
nb_execution_in_temp = False
nb_execution_timeout = 300
nb_execution_raise_on_error = False


exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "README.md", "**/.*"]
