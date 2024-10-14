from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="StrTokenizer",
    version="1.0.1", 
    author="Imon Mallik",
    author_email="imoncoding@gmail.com",
    description="A Python equivalent of Java's StringTokenizer with some added functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CyberPokemon/StrTokenizer.git",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords="string tokenizer split parse",  # Add relevant keywords
    python_requires='>=3.6',
)
