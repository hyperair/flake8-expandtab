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
    }
)
