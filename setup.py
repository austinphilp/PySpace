from codecs import open
from os import path
from setuptools import find_packages
from setuptools import setup

cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'README.md')) as f:
    long_description = f.read()

setup(
    name="space",
    version="0.0.1",
    author="Austin Philp",
    author_email="austinphilp@gmail.com",
    description="A space simulation to be programmed against",
    long_description=long_description,
    license="The MIT License (MIT)",
    url="https://github.com/allelos/vectors",
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
)
