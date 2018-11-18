# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='python-leanplum',
    version='0.4.2',
    description='python leanplum SDK',
    long_description=readme,
    author='Jesse Li / Eric Pluntze',
    author_email='eric@sandboxx.com',
    url='https://github.com/sandboxxapp/leanplum-python',
    license=license,
    packages=find_packages(exclude='examples'),
    install_requires=required
)
