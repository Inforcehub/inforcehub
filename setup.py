#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

readme = open("README.rst").read()
# doclink = """
# Documentation
# -------------

# The full documentation is at http://inforcehub.rtfd.org."""
githublink = """
Github repository
-----------------

The code can be found on GitHub at https://github.com/Inforcehub/inforcehub."""
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="inforcehub",
    version="0.2.0",
    description="Utilities for data science and customer management",
    long_description=readme + "\n\n" + githublink + "\n\n" + history,
    author="inforcehub",
    author_email="matt.gosden@inforcehub.com",
    url="https://github.com/inforcehub/inforcehub",
    packages=["inforcehub"],
    package_dir={"inforcehub": "inforcehub"},
    include_package_data=True,
    install_requires=[],
    license="GNU",
    zip_safe=False,
    keywords="inforcehub",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
