from platform import python_revision
from setuptools import setup

setup(
    name="data_pkg",
    version="0.0.1",
    author="Arthur Elmes",
    description="Example package",
    long_description="This is an example package",
    url="www.arthurelmes.com",
    keywords="test, sample",
    python_requires=">=3.8, <4",
    package_dir={"data_pkg": "data_analysis"},
    include_package_data=True,
    package_data={"": ["data/*.csv"]}
)