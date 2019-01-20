from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="TLUtils",
    version="0.1.0",
    author="tianliang",
    author_email="tianliangjay@gmail.com",
    description="some analysis and visualize utils code for pytorch coding",
    # long_description=open("README.rst").read(),
    license="MIT",
    url="https://github.com/xingkongliang/TLUtils",
    packages=find_packages(),
    zip_safe=False,
)

install_requires=[
        'six>=1.5.2',
    ]
