#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Le Duc Nam",
    author_email='lenam.k54@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Using GUI for converting PDF to some format with editable like docx, pptx, xlsx, ... ",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pdf_converter_gui',
    name='pdf_converter_gui',
    packages=find_packages(include=['pdf_converter_gui', 'pdf_converter_gui.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lenam.k54/pdf_converter_gui',
    version='0.1.0',
    zip_safe=False,
)
