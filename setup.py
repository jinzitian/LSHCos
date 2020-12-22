# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages
import lshcos

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


required = ['numpy']

setup(
    name='lshcos',
    version=lshcos.__version__,
    packages=['lshcos'],
    author='Chef_J',
    author_email='hedge_jzt@hotmail.com',
    maintainer='Chef_J',
    maintainer_email='hedge_jzt@hotmail.com',
    description='A fast Python implementation of locality sensitive hashing with cosine distance.',
    long_description=readme + '\n\n' + changes,
    license=license,
    requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        ],
)