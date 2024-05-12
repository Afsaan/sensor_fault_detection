from setuptools import find_packages, setup
from typing import List

## find_packages is responsible for checking all the packages that are present inside a main folder

setup(
    name = "sensor", # project name
    version = "0.0.1",
    author = "Afsan",
    author_email = "khanaafsaan11@gmail.com",
    packages = find_packages(),
    install_requires = ["pymongo"]
) 

# to run this setup file
# >> python setup.py install