Internal (Admin)
================

Project Management
~~~~~~~~~~~~~~~~~~

Register on `trello.com <https://trello.com/>`_ and contact `Sebastian Schwindt`_ with your request to join the project team. Include if you also aim at contributing to the web-docs (below) that are managed on `GitHub <https://github.com/sschwindt/econnect/>`_.


Web-docs
========

.. _contribute:

How to document
~~~~~~~~~~~~~~~~

This page uses *Sphinx* `readthedocs <https://readthedocs.org/>`_ and the documentation regenerates automatically after pushing changes to the repositories ``main`` branch.

To set styles, configure or add extensions to the documentation use ``ROOT/.readthedocs.yml`` and ``ROOT/docs/conf.py``.

Functions and classes are automatically parsed for `docstrings <https://www.python.org/dev/peps/pep-0257/>`_ and implemented in the documentation. Python code docs are implemented via `google style <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_ of `docstrings in scripts <https://hydro-informatics.github.io/hypy_pystyle.html#docstrings>`_. Please familiarize with the style format and strictly apply in all commits.

To modify this documentation file, edit ``ROOT/docs/index.rst`` (uses `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format).

In the class or function docstrings use the following section headers:

* ``Args`` (alias of ``Parameters``)
* ``Arguments`` (alias of ``Parameters``)
* ``Attention``
* ``Attributes``
* ``Caution``
* ``Danger``
* ``Error``
* ``Example``
* ``Examples``
* ``Hint``
* ``Important``
* ``Keyword Args`` (alias of ``Keyword Arguments``)
* ``Keyword Arguments``
* ``Methods``
* ``Note``
* ``Notes``
* ``Other Parameters``
* ``Parameters``
* ``Return`` (alias of ``Returns``)
* ``Returns``
* ``Raise`` (alias of ``Raises``)
* ``Raises``
* ``References``
* ``See Also``
* ``Tip``
* ``Todo``
* ``Warning``
* ``Warnings`` (alias of ``Warning``)
* ``Warn`` (alias of ``Warns``)
* ``Warns``
* ``Yield`` (alias of ``Yields``)
* ``Yields``

For local builds of the documentation, the following packages are required:

.. code:: console

   sudo apt install build-essential
   sudo apt install python-dev python-pip python-setuptools
   sudo apt install libxml2-dev libxslt1-dev zlib1g-dev
   apt-cache search libffi
   sudo apt install -y libffi-dev
   sudo apt install python3-dev default-libmysqlclient-dev
   sudo apt install python3-dev
   sudo apt install redis-server

To generate a local html version of the documentation, ``cd`` into the  ``docs`` directory  and type:

.. code:: console

   make html

Learn more about *Sphinx* documentation and the automatic generation of *Python* code docs through docstrings in the tutorial provided at `github.com/sschwindt/docs-with-sphinx <https://github.com/sschwindt/docs-with-sphinx>`_.


Add new Python scripts
~~~~~~~~~~~~~~~~~~~~~~

All contributors, please respect the *Zen of Python* (``import this``).

How to add new package or library imports:

* Add it to the global import management file (*ROOT/import_mgmt.py*) within an *try-except-ImportError* statement (`read more <https://hydro-informatics.github.io/hypy_pyerror.html#try-except>`_).
* If you need to import a library or package that is not yet listed in the *ROOT/environments.yml* and *ROOT/requirements.txt* files, please make sure to add the new library or package in both files.
* Add the new library or package to the ``autodoc_mock_imports`` *list* in *ROOT/docs/conf.py*.
* Update the `version number <https://www.python.org/dev/peps/pep-0440/>`_ according to the `CONTRIBUTING <https://github.com/Ecohydraulics/flusstools-pckg/blob/main/docs/CONTRIBUTING.md>`_ standards.

Please use *PEP 8* for any code (read more on `hydro-informatics.github.io/hypy_pystyle <https://hydro-informatics.github.io/hypy_pystyle.html>`_) and try to keep the number of lines per script below 150 (it's hard or even apparently impossible sometimes - just try please).

.. important::

    Only push debugged code - Thank you!

.. _Sebastian Schwindt: https://sebastian-schwindt.org/
