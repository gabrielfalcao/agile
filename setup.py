#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


install_requires = [
    'mock',
    'coverage',
    'nose',
    'rednose',
    'sure',
    'steadymark',
    'httpretty'
]


if __name__ == '__main__':
    setup(
        name='agile',
        version='1.2.0',
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
