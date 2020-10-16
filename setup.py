#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Automatic setup for custom Jupyter CSS

Authored by Eric Easthope
All rights reserved.
"""

from setuptools import setup
import os

# import sys
# import jupyter_core
import subprocess
from shutil import copyfile


def _post_install(setup):
    def _post_actions():
        # Get Jupyter notebook config directory
        command = "jupyter --config-dir"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        config_dir = output.decode("utf-8").replace("\n", "")

        # Get path to Jupyter notebook custom CSS
        custom_path = os.path.join(config_dir, "custom")

        # Get path to Darkglow theme CSS
        darkglow_path = os.path.join(os.getcwd(), "css", "darkglow.css")

        # Copy theme to replace Jupyter notebook custom CSS
        copyfile(darkglow_path, os.path.join(custom_path, "custom.css"))

    _post_actions()
    return setup


_post_install(
    setup(
        name="nbstyle",
        version="0.0.1",
        author="Eric Easthope",
        include_package_data=True,
    )
)
