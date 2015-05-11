#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


install_requires = [
    'mock==1.0.1',
    'coverage',
    'nose==1.3.4',
    'rednose==0.4.1',
    'sure==1.2.12',
    'steadymark',
    'httpretty'
]


if __name__ == '__main__':
    setup(
        name='agile',
        version='1.3.1',
        description=(
            'A meta-package containing a full toolset for agile development with TDD'
        ),
        author='Gabriel Falcao',
        author_email='gabriel@nacaolivre.org',
        include_package_data=True,
        url='http://github.com/gabrielfalcao/agile',
        packages=[],
        install_requires=install_requires,
    )
