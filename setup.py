#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup(
    name="i_learned_stuff",
    author="Alex Silver",
    author_email='thirdformant@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    license="MIT license",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        "jsonpickle"
    ],
    entry_points='''
        [console_scripts]
        learn_commit=i_learned_stuff.cli:main
    ''',
)
