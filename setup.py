# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages
import lshcos

with open('README.rst') as f:
    readme = f.read()


setup(
    name='lshcos',
    version=lshcos.__version__,
    packages=['lshcos'],
    author='Chef_J',
    author_email='hedge_jzt@hotmail.com',
    maintainer='Chef_J',
    maintainer_email='hedge_jzt@hotmail.com',
    description='A fast Python implementation of locality sensitive hashing with cosine distance.',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/jinzitian/LSHCos',
    install_requires=['numpy'],

)