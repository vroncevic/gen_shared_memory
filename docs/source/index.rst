Generate shared memory segments
---------------------------------

**gen_shared_memory** is framework for generation shared memory segments modules.

Developed in `python <https://www.python.org/>`_ code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_shared_memory python checker| |gen_shared_memory python package| |github issues| |documentation status| |github contributors|

.. |gen_shared_memory python checker| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python_checker.yml

.. |gen_shared_memory python package| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_shared_memory.svg
   :target: https://github.com/vroncevic/gen_shared_memory/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_shared_memory.svg
   :target: https://github.com/vroncevic/gen_shared_memory/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen_shared_memory/badge/?version=latest
   :target: https://gen-shared-memory.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_shared_memory python3 build|

.. |gen_shared_memory python3 build| image:: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_shared_memory/actions/workflows/gen_shared_memory_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_shared_memory/releases

To install package type the following

.. code-block:: bash

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
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_shared_memory_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_shared_memory_run.py /usr/local/bin/gen_shared_memory_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    # pyton3
    pip3 install gen_shared_memory

Dependencies
-------------

**gen_shared_memory** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure

**gen_shared_memory** is based on OOP.

.. code-block:: bash

    gen_shared_memory/
           ├── conf/
           │   ├── gen_shared_memory.cfg
           │   ├── gen_shared_memory.logo
           │   ├── gen_shared_memory_util.cfg
           │   ├── project.yaml
           │   └── template/
           │       ├── client.template
           │       ├── Makefile.template
           │       ├── server.template
           │       └── shared_memory.template
           ├── __init__.py
           ├── log/
           │   └── gen_shared_memory.log
           ├── pro/
           │   ├── __init__.py
           │   ├── read_template.py
           │   └── write_template.py
           ├── py.typed
           └── run/
               └── gen_shared_memory_run.py

Copyright and licence
----------------------

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