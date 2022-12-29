"""Configuration file for the Sphinx documentation builder."""

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# put parent folder in path so that sphinx can find the code to document
sys.path.append(os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'm269-library'
copyright = '2017–2022, Michel Wermelinger'
author = 'Michel Wermelinger'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
]
source_suffix = ['.rst', '.md']

# templates_path = ['_templates']
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    # Alabaster
    # 'github_user': "mwermelinger",
    # 'github_repo': "m269-library",
    # 'github_button': True,
    # 'description': "A pedagogical algorithms and data structures library.",

    # Book theme
    # "repository_url": "https://github.com/mwermelinger/m269-library",
    # "use_repository_button": True,
}

# html_static_path = ['_static']

# Don't copy reST source to HTML output
html_copy_source = False
