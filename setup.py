# coding=utf-8

"""
pyIMU a python library for Pololu MEMS xIMU sensors

Copyright 2019, Marcin Filip Wiśniowski
Licensed under Apache 2.0 license.
"""

import setuptools

version = "0.1.0.dev1"

with open("README.md", "r") as fulld:
    long_description = fulld.read()

setuptools.setup(
    name="pyIMU",
    version=version,
    author="Marcin F. Wiśniowski",
    author_email="marcin.wisniowski@mfw.pl",
    description="Python library for Pololu MEMS xIMU-x sensors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcinwisniowski/pyIMU",
    packages=setuptools.find_packages(),
    keywords="pololu altimu10 minimu9 mems sensors gyro altimeter accelerometer magnetometer raspberry",
    license="Apache Software License 2.0",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    project_urls={
        "Source": "https://github.com/marcinwisniowski/pyIMU",
        "Tracker": "https://github.com/marcinwisniowski/pyIMU/issues",
    },
    install_requires=["smbus"]
)
