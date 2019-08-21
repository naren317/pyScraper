
import os

from setuptools import setup

DEPENDENCY_FILE = 'ProgramDependencies.config'

requires = []

if os.path.isfile(DEPENDENCY_FILE):
    with open(DEPENDENCY_FILE) as f:
        requires = f.read().splitlines()


    setup(name="Scraper", install_requires=requires)

else:
 print("Dependency file - ProgramDependencies.config - not found !!!")
