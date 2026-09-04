# Generate Shared Memory Segments

<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_shared_memory/dev/docs/gen_shared_memory_logo.png" width="25%">

**gen_shared_memory** is toolset for generation of shared memory segment modules.

Developed in **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_shared_memory python checker](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python_checker.yml/badge.svg)](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python_checker.yml) [![gen_shared_memory package checker](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_package_checker.yml/badge.svg)](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_package.yml) [![gen_shared_memory interface checker](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_interface_checker.yml/badge.svg)](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_interface_checker.yml) [![gen_shared_memory isp checker](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_isp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_isp_checker.yml) [![gen_shared_memory srp checker](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_srp_checker.yml/badge.svg)](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_srp_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_shared_memory.svg)](https://github.com/vroncevic/gen_shared_memory/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_shared_memory.svg)](https://github.com/vroncevic/gen_shared_memory/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [🚀 Installation](#-installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [📦 Dependencies](#-dependencies)
- [📁 Tool structure](#-tool-structure)
  - [✨ Features](#-features)
- [📊 Code coverage](#-code-coverage)
- [🛠 Usage](#-usage)
- [📚 Docs](#-docs)
- [👥 Contributing](#-contributing)
- [📄 Copyright and licence](#-copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### 🚀 Installation

Used next development environment

![debian linux os](https://raw.githubusercontent.com/vroncevic/gen_shared_memory/dev/docs/debtux.png)

[![gen_shared_memory python3 build](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python3_build.yml/badge.svg)](https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

**gen_shared_memory** is located at **[pypi.org](https://pypi.org/project/gen_shared_memory/)**.

You can install by using pip

```bash
# python3
pip3 install gen_shared_memory
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_shared_memory/releases/)** download and extract release archive.

To install **gen_shared_memory** type the following

```bash
tar xvzf gen_shared_memory-x.y.z.tar.gz
cd gen_shared_memory-x.y.z/
# python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py 
python3 -m pip install --upgrade setuptools
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
pip3 install -r requirements.txt
python3 -m build --no-isolation --wheel
pip3 install ./dist/gen_shared_memory-*-py3-none-any.whl
rm -f get-pip.py
```

##### Install using py setup

Navigate to **[release page](https://github.com/vroncevic/gen_shared_memory/releases)** download and extract release archive.

To install **gen_shared_memory** locate and run setup.py with arguments

```bash
tar xvzf gen_shared_memory-x.y.z.tar.gz
cd gen_shared_memory-x.y.z
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container.

### 📦 Dependencies

**gen_shared_memory** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://pypi.org/project/ats-utilities/)

### 📁 Tool structure

**gen_shared_memory** is based on OOP.

Tool structure

<details>
<summary><b>Click to expand framework structure</b></summary>

```bash
    gen_shared_memory/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── __init__.py
         │   │   └── project_setup.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── command.py
         │   │   ├── gen_shared_memory_command_definition.py
         │   │   ├── gen_shared_memory_command_executor.py
         │   │   ├── icommand_definition.py
         │   │   ├── icommand_executor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_shared_memory.cfg
         │   │   ├── gen_shared_memory.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── __init__.py
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 45 files
```
</details>

#### ✨ Features

* Automatically scaffolds POSIX shared memory projects with clean, standardized C code (`server.c`, `client.c`, `shared_memory.h`, `Makefile`).
* Provides a modular and extensible architecture based on OOP and SOLID principles (Hexagonal / Ports & Adapters).
* Includes command line interface (CLI) support via a command/executor structure.
* Robust validation of project bundles, dependencies, and options.
* Modern template system using gzip archive (`templates.tgz`) and JSON configuration schema (`scheme.json`).
* High code quality with full type annotations, 10.00/10 Pylint score, and 100% unit test coverage.

### 📊 Code coverage

<details>
<summary><b>Click to expand code coverage</b></summary>

| Name | Stmts | Miss | Cover |
|------|-------|------|-------|
| `gen_shared_memory/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/core/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/core/model/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/core/model/project_setup.py` | 14 | 0 | 100%|
| `gen_shared_memory/core/service/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/core/service/engine.py` | 27 | 0 | 100%|
| `gen_shared_memory/core/service/iservice.py` | 14 | 0 | 100%|
| `gen_shared_memory/core/service/isubprocessor.py` | 14 | 0 | 100%|
| `gen_shared_memory/engine.py` | 57 | 0 | 100%|
| `gen_shared_memory/infrastructure/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/engine.py` | 38 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/icli.py` | 14 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/bundle.py` | 22 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/dependencies.py` | 18 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/factory.py` | 35 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/keys.py` | 26 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/opt_validator.py` | 36 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/options.py` | 15 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/registry.py` | 24 | 0 | 100%|
| `gen_shared_memory/infrastructure/cli/setup/validator.py` | 43 | 0 | 100%|
| `gen_shared_memory/infrastructure/command/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/infrastructure/command/command.py` | 16 | 0 | 100%|
| `gen_shared_memory/infrastructure/command/gen_shared_memory_command_definition.py` | 24 | 0 | 100%|
| `gen_shared_memory/infrastructure/command/gen_shared_memory_command_executor.py` | 23 | 0 | 100%|
| `gen_shared_memory/infrastructure/command/icommand_definition.py` | 14 | 0 | 100%|
| `gen_shared_memory/infrastructure/command/icommand_executor.py` | 14 | 0 | 100%|
| `gen_shared_memory/infrastructure/subprocessor.py` | 57 | 0 | 100%|
| `gen_shared_memory/setup/__init__.py` | 9 | 0 | 100%|
| `gen_shared_memory/setup/bundle.py` | 23 | 0 | 100%|
| `gen_shared_memory/setup/dep_validator.py` | 36 | 0 | 100%|
| `gen_shared_memory/setup/dependencies.py` | 19 | 0 | 100%|
| `gen_shared_memory/setup/factory.py` | 48 | 0 | 100%|
| `gen_shared_memory/setup/keys.py` | 27 | 0 | 100%|
| `gen_shared_memory/setup/opt_validator.py` | 34 | 0 | 100%|
| `gen_shared_memory/setup/options.py` | 12 | 0 | 100%|
| `gen_shared_memory/setup/registry.py` | 32 | 0 | 100%|
| `gen_shared_memory/setup/validator.py` | 48 | 0 | 100%|
| **Total** | 941 | 0 | 100% |

</details>

### 🛠 Usage

Install package

```bash
pip3 install gen_shared_memory
```

Prepare main entry point by downloading [main.py](https://raw.githubusercontent.com/vroncevic/gen_shared_memory/main/main.py) or create your own.

```bash
wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_shared_memory/main/main.py
```

Running tool for creating new shared memory project:

```bash
python3 main.py create --name myshm --output ./demo/
```

### 📚 Docs

[![Documentation Status](https://readthedocs.org/projects/gen-shared-memory/badge/?version=latest)](https://gen-shared-memory.readthedocs.io/en/latest/?badge=latest)

More documentation and info at

* [gen-shared-memory.readthedocs.io](https://gen-shared-memory.readthedocs.io)
* [www.python.org](https://www.python.org/)

### 👥 Contributing

[Contributing to gen_shared_memory](CONTRIBUTING.md)

### 📄 Copyright and licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2018 - 2026 by [vroncevic.github.io/gen_shared_memory](https://vroncevic.github.io/gen_shared_memory)

**gen_shared_memory** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_shared_memory/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.python.org/psf/donations/)