# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Examen_Entornos'
copyright = '2024, Alejandro Ruiz'
author = 'Alejandro Ruiz'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',     # Para generar documentación automáticamente a partir de docstrings
    'sphinx.ext.intersphinx', # Para enlazar la documentación con otros proyectos
    'sphinx.ext.todo',        # Para incluir y gestionar todo items
    'sphinx.ext.mathjax',     # Para renderizar fórmulas matemáticas
    'sphinx.ext.napoleon',    # Para soportar Google y NumPy estilo docstrings
    'sphinx.ext.autosummary', # Para generar automáticamente resúmenes
]
templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
