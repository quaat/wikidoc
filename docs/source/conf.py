# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Knowledge Base'
copyright = '© SINTEF 2022'
author = 'SINTEF'
release = '0.0.1'
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


# General configuration
extensions = [
    "myst_parser",  # markdown source support
    "sphinx.ext.autodoc",  # API ref
    "sphinx.ext.napoleon",  # API ref Google and NumPy style
    "sphinx.ext.viewcode",  # API link to source
    "sphinx.ext.graphviz",  # Graphviz
    "sphinxcontrib.plantuml",  # PlantUml
    "sphinx_copybutton",  # Copy button for codeblocks
    "nbsphinx",  # Jupyter
    "IPython.sphinxext.ipython_console_highlighting",  # nb syntax highlight
    "sphinx.ext.autosectionlabel",  # Auto-generate section labels.
    "sphinx_panels",  # Create panels in a grid layout or as drop-downs
    "sphinx_markdown_tables",
]

master_doc = "index"

myst_heading_anchors = 5

plantuml = "java -jar lib/plantuml.jar"
plantuml_output_format = "svg_img"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# HTML output
html_theme = "sphinx_book_theme"
html_logo = "_static/logo.jpg"
html_favicon = "_static/favicon.ico"
html_theme_options = {
    "repository_url": "https://gitlab.sintef.no/sintef/docs",
    "use_repository_button": True,
    "repository_branch": "main",
    "path_to_docs": "docs",
    "logo_only": True,
    "show_navbar_depth": 2,
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]

nbsphinx_allow_errors = True

suppress_warnings = ["myst.mathjax"]
