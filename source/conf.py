import os
import sys
sys.path.insert(0, os.path.abspath('../../optimizador_joshua_2'))

# -- Project information -----------------------------------------------------
project = 'optimizador_joshua_2'
copyright = '2024, Joshua Rodriguez'
author = 'Joshua Rodriguez'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

