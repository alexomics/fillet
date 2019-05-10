# fillet
---
## Table of Contents

<details>
<summary>Click to expand</summary>
<p>

- [Introduction](#introduction)
- [Installation](#installation)
  - [PyPI](#installing-fillet-with-pypi)
  - [GitHub](#installing-fillet-from-github)
- [Usage](#usage)
</p>
</details>

## Introduction

fillet is a simulation manager for Oxford Nanopore Technologies MinKNOW software, making adding simulation devices and
playback runs easier

## Installation

### Installing fillet with PyPI

```bash
pip install fillet
```

### Install fillet from GitHub

```bash
git clone https://github.com/alexomics/fillet
cd fillet
python setup.py install
```

## Usage

fillet installs with a terminal entry point as `fillet`

Add a bulk FAST5 file for simulation:
```bash
fillet sim -t <MinKNOW_config_filename> -b <bulk_file_to simulate>
```
Remove a bulk FAST5 file for simulation:
```bash
fillet sim -t <MinKNOW_config_filename>
```

Add a simulation device:
```bash
fillet add
```
Remove a simulation device:
```bash
fillet add -r
```
