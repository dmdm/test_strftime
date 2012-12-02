#!/usr/bin/env python
from setuptools import setup

requires = ['six']

setup(
    name="test_strftime",
    version="1",
    packages=[],
    include_package_data=True,
    install_requires=requires,
    test_suite='tests'
)
