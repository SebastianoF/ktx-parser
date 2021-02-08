import os

from setuptools import find_packages, setup


with open("README.md") as f:
    readme = f.read()

with open("requirements.txt") as f:
    requirements = f.readlines()

setup(
    name="ktx-parser",
    version="0.0.0beta",
    description="Keyed text parser",
    long_description=readme,
    author="Sebastiano Ferraris",
    author_email="sebastiano.ferraris@gmail.com",
    url="https://github.com/SebastianoF",
    packages=find_packages(exclude=["examples", "tests"]),
    python_requires=">=3.7",
    install_requires=requirements,
    include_package_data=False,
    keywords="parsers",
    classifiers=[
        "Intended Audience :: Developers/Researchers",
        "Language :: English",
        "Programming Language :: Python :: 3",
    ],
)
