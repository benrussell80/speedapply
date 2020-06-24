#!/usr/bin/env python3
import os
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    README = fh.read()

setup(
    # change project name
    name="speedapply",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'speedapply=speedapply.__main__:main',
        ]
    },
    install_requires=[
        'selenium',
        'beautifulsoup4'
    ],
    include_package_data=True,
    author="Ben Russell",
    author_email="bprussell80@gmail.com",
    description="Package for automatically applying to relevant jobs on popular job boards.",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords="job applications",
    url="https://github.com/benrussell80/speedapply",
    project_urls={
        "Source Code": "https://github.com/benrussell80/speedapply"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)