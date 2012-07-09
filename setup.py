#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import authoritarian

try:
    from setuptools import setup
    hush_pyflakes = setup
except ImportError:
    from distutils.core import setup
   

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

required = [
    'requests==0.13.2', 'omnijson==0.1.2',
]

setup(
    name='authoritarian',
    version=authoritarian.__version__,
    description='Python API for the AuthorityLabs Partner API.',
    long_description="""
    **authoritarian** is a Python client implementation of the `AuthorityLabs Partner API <http://authoritylabs.com/api/partner-api/`_.

    Source Code: `https://github.com/michaeljoseph/authoritarian <https://github.com/michaeljoseph/authoritarian>`_

    RTFD: `http://authoritarian.readthedocs.org <http://authoritarian.readthedocs.org>`_
    """,
    author=authoritarian.__author__,
    author_email='michaeljoseph@gmail.com',
    url='https://github.com/michaeljoseph/authoritarian',
    packages= [
        'authoritarian',
    ],
    install_requires=required,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
    ),
)

