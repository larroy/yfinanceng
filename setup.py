#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Yahoo! Finance ng python / pandas market data downloader

"""Yahoo! Finance market data downloader (+fix for Pandas Datareader)"""

from setuptools import setup, find_packages

# from codecs import open
import io
from os import path


INSTALL_REQUIRES = [
    "pandas>=0.24",
    "numpy>=1.15",
    "requests>=2.20",
    "multitasking>=0.0.7",
    "lxml",
    "beautifulsoup4==4.9.0",
    "html5lib",
]
EXTRAS_REQUIRE = {"test": ["tox", "flake8", "black", "mock", "pre-commit", "nose", "pytest"]}


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="yfinanceng",
    version="0.1.58",
    description="Yahoo! Finance market data downloader",
    long_description=long_description,
    url="https://github.com/larroy/yfinanceng",
    author="Ran Aroussi",
    author_email="pedro.larroy.lists@gmail.com",
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    platforms=["any"],
    keywords="pandas, yahoo finance, pandas datareader",
    packages=find_packages(exclude=["contrib", "docs", "tests", "examples", "util"]),
    # packages=find_packages("yfinanceng"),
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.6",
    entry_points={"console_scripts": ["sample=sample:main",],},
)
