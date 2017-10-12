#!/usr/bin/env python

from distutils.core import setup

setup(
    name='flake8-expandtab',
    version='0.1',
    description='flake8 for tab junkies',
    author='Chow Loong Jin',
    author_email='hyperair@debian.org',
    url='https://www.github.com/hyperair/flake8-expandtab',
    entry_points={
        'flake8.extension': [
            'expandtab = expandtab:TabExpander',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Operating System :: OS Independent"
    ]
)
