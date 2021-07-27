#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup for RobotAtVirtualHome API
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robotatvirtualhome",
    version="0.1.0",
    author="D. Fernandez Chaves",
    author_email="davfercha@uma.es",
    description="'This package provides Python API that assists in loading the annotations in Robot@VirtualHome Dataset",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "numpy",
        "pillow >= 5.2"
    ],
    python_requires='>=3.7',
)
