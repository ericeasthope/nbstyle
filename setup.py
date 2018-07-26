#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
setup(
    name="nbstrux",
    packages=['nbstyle'],
    package_dir={
        'nbstyle': 'nbstyle/nbstyle'
        },
    package_data={
        'nbstyle': ['static/*']
        },
    include_package_data=True
)
