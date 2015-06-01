#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'ocs_ansible',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [ 'scaleway-sdk' ],
    entry_points = {
      'console_scripts': [ 'scw_inventory=ocs_ansible:main' ]
    }
)
