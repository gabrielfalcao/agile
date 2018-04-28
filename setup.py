#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


local_file = lambda *f: \
    open(os.path.join(os.path.dirname(__file__), *f)).read()


install_requires = local_file('dependencies.txt').splitlines()


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
        url='http://github.com/gabrielfalcao/agile',
        packages=[],
        include_package_data=True,
        install_requires=install_requires,
    )
