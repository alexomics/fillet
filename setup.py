from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md")) as fh:
    long_description = fh.read()

exec(open("fillet/version.py").read())

setup(
    name="fillet",
    version=__version__,
    author="Alexander Payne",
    author_email="alexander.payne@nottingham.ac.uk",
    description="Assistance scripts for ONT MinKNOW",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexomics/fillet",
    packages=find_packages(),
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "fillet=fillet.main:main",
        ],
    },
    package_dir={"fillet": "fillet"},
    install_requires=["toml",]  # TODO: give version numbers
)
