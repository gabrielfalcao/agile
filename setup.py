#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


install_requires = [
    "couleur==0.6.2",
    "coverage==4.2",
    "httpretty==0.8.14",
    "mock==2.0.0",
    "nose==1.3.7",
    "rednose==1.2.1",
    "steadymark==0.7.3",
    "sure==1.4.0",
]


if __name__ == '__main__':
    setup(
        name='agile',
        version='1.4.0',
        description=(
            'A meta-package containing a full '
            'toolset for agile development with TDD'
        ),
        author='Gabriel Falcao',
        author_email='gabriel@nacaolivre.org',
        include_package_data=True,
        url='http://github.com/gabrielfalcao/agile',
        packages=[],
        install_requires=install_requires,
    )
