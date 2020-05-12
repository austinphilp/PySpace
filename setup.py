from codecs import open
from os import path
from setuptools import find_packages
from setuptools import setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md')) as f:
    long_description = f.read()

setup(
    name="space",
    version="0.0.1",
    author="Austin Philp",
    author_email="austinphilp@gmail.com",
    description="A space simulation to be programmed against",
    long_description=long_description,
    license="The MIT License (MIT)",
    url="https://github.com/austinphilp/pyspace",
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
)
