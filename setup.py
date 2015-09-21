#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.languages',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.languages'],
    version='0.01',
    description='Python tools for working with languages (specifically RFC5646) and Who\'s On First data',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-languages',
    install_requires=[
        'requests',
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-languages-compile-subtags',
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-languages/releases/tag/v0.01',
    license='BSD')
