# setup.py

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="StrTokenizer",
    version="1.0.0", 
    author="Imon Mallik",
    author_email="imoncoding@gmail.com",
    description="A Python equivalent of Java's StringTokenizer with some added functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CyberPokemon/StrTokenizer.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
