#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = ['cryptography']

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='PySimpleAES',
    version='0.0.1',
    description=('Python AES encryptation'),
    long_description=readme + '\n\n' + history,
    author="Fabricio Roberto reinert",
    author_email='fabricio.reinert@live.com',
    url='https://github.com/FRReinert/AES',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='Python, AES, cryptography',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests.test_app.tests',
    tests_require=test_requirements
)
