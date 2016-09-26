#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests',
    'RISparser>=0.4.1',
    'XlsxWriter>=0.7.3',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='litter_getter',
    version='0.1.0',
    description="Retrieve literature from biomedical reference libraries such as PubMed, EPA's HERO, and imports from Endnote RIS exports",
    long_description=readme + '\n\n' + history,
    author="Andy Shapiro",
    author_email='shapiromatron@gmail.com',
    url='https://github.com/shapiromatron/litter_getter',
    packages=[
        'litter_getter',
    ],
    package_dir={'litter_getter': 'litter_getter'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='litter_getter',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
