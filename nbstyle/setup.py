#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Removes redundant UI elements, changes notebook style sheets
"""

from setuptools import setup, find_packages
setup(
    name="nbstyle",
    version='0.0.dev0',
    author='Eric Easthope',
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/nbstyle", [
            "nbstyle/static/main.js",
        ]),
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/nbstyle", [
            "nbstyle/static/restyle.css",
        ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/notebook.d", [
            "jupyter-config/nbconfig/notebook.d/nbstyle.json"
        ]),
        # like `jupyter serverextension enable --sys-prefix`
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/nbstyle.json"
        ]),
    ],
    zip_safe=False
)
