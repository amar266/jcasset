#!/usr/bin/python

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='jcasset',
    version='0.1',
    description='DataCenter Assets Management',
    author='Amar Krishna',
    author_email='Amar.Krishna@ril.com',
    url='http://github.com/amar266/jcasset',
    packages=find_packages(),
    include_package_data=True,
    license='Apache 2.0',
    keywords='Datacenter Assets',
    install_requires=install_requires,
)
