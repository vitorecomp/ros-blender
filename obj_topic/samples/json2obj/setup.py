# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup

requirements = open("requirements/requirements.txt", "rt").readlines()

with io.open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setup(
    name="json2obj",
    version=1.0,
    author="Vieira, Vitor",
    author_email="vitor.ecomp@gmail.com",
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    url="https://github.com/vitorecomp/ros-blender",
    license="COPYRIGHT",
    description="Simple JSON to Waveform(.obj) converter.",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
        "dev": requirements,
    },
    python_requires=">=3.6",
    classifiers=[
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
    ],
    keywords=(),
    entry_points={
        "console_scripts": ["json2obj = json2obj.__main__:start"],
    },
)