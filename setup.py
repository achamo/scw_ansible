#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'scw_ansible',
    version = '0.0.2',
    packages = find_packages(),
    install_requires = [ 'scaleway-sdk' ],
    entry_points = {
      'console_scripts': [ 'scw_inventory=scw_ansible:main' ]
    }
)
