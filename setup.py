#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Automatic setup for custom Jupyter CSS

Authored by Eric Easthope
All rights reserved.
"""

# from setuptools import setup, find_packages
import os
import jupyter_core
from shutil import copyfile

# Get path to Jupyter notebook custom CSS
custom_path = os.path.join(jupyter_core.paths.jupyter_config_dir(), "custom")

# Get path to Darkglow theme CSS
darkglow_path = os.path.join(os.getcwd(), "css", "darkglow.css")

# Copy theme to replace Jupyter notebook custom CSS
copyfile(darkglow_path, os.path.join(custom_path, "custom.css"))

"""
setup(
    name="nbstyle",
    version="0.0.1",
    author="Eric Easthope",
    include_package_data=True,
)
"""
