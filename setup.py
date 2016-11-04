#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.languages.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst.languages',
    namespace_packages=['mapzen', 'mapzen.whosonfirst'],
    description='Python tools for working with languages (specifically RFC5646) and Who\'s On First data',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-languages',
    install_requires=[
        'requests',
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-languages-compile-subtags',
        'scripts/wof-languages-compile-iso639-codes',
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-languages/releases/tag/' + version,
    license='BSD')
