# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages
import lshcos

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst',encoding = 'utf-8') as f:
    readme = f.read()

with open('LICENSE.txt') as f:
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
    long_description=readme,
    long_description_content_type='text/plain/markdown',
    license=license,
    requires=required,
    url='https://github.com/jinzitian/LSHCos',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        ],
)