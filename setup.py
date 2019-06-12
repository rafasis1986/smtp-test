#!/usr/bin/env python
from setuptools import find_packages, setup

project = "smtp_test"
version = "0.1.0"

setup(
    name=project,
    version=version,
    description="A sendmail library with sockets.",
    author="Rafael Torres",
    author_email="rdtr.sis@gmail.com",
    url="https://github.com/rafasis1986/smtp-test",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    setup_requires=[
        "nose>=1.3.6",
    ],
    dependency_links=[
    ],
    entry_points={
    },
    extras_require = {
        "test": [
            "coverage>=3.7.1",
            "mock>=1.0.1",
            "PyHamcrest>=1.8.5",
        ],
    },
)
