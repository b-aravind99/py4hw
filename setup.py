# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='py4hw',
    version='0.0.1',
    author='Universitat Autonoma de Barcelona',
    author_email='david.castells@uab.cat',
    description='py4hw is a library to model, and simulate digital logic circuits. It propomotes the use of structural design description to build hardware, and it is highly influenced by the ideas behind JHDL.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/davidcastells/py4hw',
    install_requires=open('requirements.txt').readlines(),
    tests_require=open('requirements.txt').readlines(),
    packages=find_packages()
)