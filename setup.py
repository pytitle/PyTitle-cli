#!/usr/bin/env python3
import importlib
import pathlib

from setuptools import find_packages, setup

WORK_DIR = pathlib.Path(__file__).parent


def get_version():
    """
    Read version
    :return: str
    """
    return importlib.import_module("pytitle_cli").__version__


def get_description():
    """
    Read full description from 'README.md'
    :return: description
    :rtype: str
    """
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="pytitle",
    version=get_version(),
    packages=find_packages(
        exclude=(
            "tests",
            "tests.*",
            "examples.*",
            "docs",
        )
    ),
    url="https://github.com/sina-e/pytitle_cli",
    license="MIT",
    author="Sina Ebrahimi",
    python_requires=">=3.8",
    author_email="ebrahimisina78@gmail.com",
    description="Command line tool for editing and manipulating subtitles.",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Multimedia :: Video",
        "Topic :: Text Processing",
        "Typing :: Typed",
    ],
    keywords=[
        "subtitle",
        "subtitles",
        "subtitle-manipulation",
        "subtitle-manipulation-library",
        "subtitle-manipulation-python",
        "srt-subtitles",
        "vtt-subtitles",
        "ssa-subtitles",
        "ass-subtitles",
        "srt",
        "vtt",
        "ass",
        "ssa",
        "subtitle-edit",
        "subtitle-editor",
    ],
    install_requires=[
        "pytitle==0.1.6",
        "typer==0.4.1",
    ],
    extras_require={},
    project_urls={
        "Documentation": "https://pytitle-cli.readthedocs.io",
        "Source": "https://github.com/sina-e/pytitle-cli",
    },
    include_package_data=False,
)
