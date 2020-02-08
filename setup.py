#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
setup(
    name="nbstyle",
    packages=['nbstyle'],
    package_dir={
        'nbstyle': 'nbstyle/nbstyle'
        },
    package_data={
        'nbstyle': ['static/*']
        },
    include_package_data=True
)
