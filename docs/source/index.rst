Generate shared memory segments
---------------------------------

**gen_shared_memory** is framework for generation shared memory segments modules.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_shared_memory python checker| |gen_shared_memory python package| |gen_shared_memory interface checker| |gen_shared_memory isp checker| |gen_shared_memory srp checker| |github issues| |documentation status| |github contributors|

.. |gen_shared_memory python checker| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python_checker.yml

.. |gen_shared_memory python package| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_package.yml

.. |gen_shared_memory interface checker| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_interface_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_interface_checker.yml

.. |gen_shared_memory isp checker| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_isp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_isp_checker.yml

.. |gen_shared_memory srp checker| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_srp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_srp_checker.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_shared_memory.svg
   :target: https://github.com/vroncevic/gen_shared_memory/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_shared_memory.svg
   :target: https://github.com/vroncevic/gen_shared_memory/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-shared-memory/badge/?version=latest
   :target: https://gen-shared-memory.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents:

   self
   modules

🚀 Installation
====================================================================

|gen_shared_memory python3 build|

.. |gen_shared_memory python3 build| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_shared_memory/releases

To install this set of modules type the following

.. code-block:: bash

    tar xvzf gen_shared_memory-x.y.z.tar.gz
    cd gen_shared_memory-x.y.z/
    # python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen_shared_memory

📦 Dependencies
====================================================================

**gen_shared_memory** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
====================================================================

**gen_shared_memory** is based on OOP

Code structure

.. code-block:: bash

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

📄 Copyright and licence
====================================================================

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2018 - 2026 by `vroncevic.github.io/gen_shared_memory <https://vroncevic.github.io/gen_shared_memory>`_

**gen_shared_memory** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_shared_memory/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`