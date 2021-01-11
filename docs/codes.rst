Methods
=======

Eco-morphological Connectivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lateral and vertical connectivity (University of Stuttgart)

More coming soon

Hydrological Connectivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Longitudinal connectivity (NCEPU/YTU)

More coming soon

Code Documentation
=========================

This section will be filled with codes products.

Data
====

Small Datasets (<100MB)
~~~~~~~~~~~~~~~~~~~~~~~

Smaller and test datasets for application examples will be provided on GitHub repositories with instructions on how to use the data with algorithms from this project.

Large Datasets (>100MB)
~~~~~~~~~~~~~~~~~~~~~~~

Large datasets will be hosted on the independent educational, and state-funded `bwSync&Share <https://bwsyncandshare.kit.edu>`_ platform. To get read and write access to the large file repository, `email Sebastian`_.

Instructions
============

Create new Code
~~~~~~~~~~~~~~~


.. sidebar:: A code example

    The Python script ``example_solver.py`` lives in the host repository of this website in ``ROOT/codes/``. The left column shows this Python script in its original form with docstrings (the ``"""This is a docstring"""``). For writing new code, please read this entire page first, follow the instructions below, and visit `hydro-informatics.github.io`_. All contributors, please respect the *Zen of Python* (``import this``). Thank you!

.. literalinclude:: example_solver.py
    :language: python
    :linenos:
    :lines: 1-20



How to add new package or library imports:

* Add it to the global import management file (*ROOT/import_mgmt.py*) within an *try-except-ImportError* statement (`read more <https://hydro-informatics.github.io/hypy_pyerror.html#try-except>`_).
* If you need to import a library or package that is not yet listed in the *ROOT/environments.yml* and *ROOT/requirements.txt* files, please make sure to add the new library or package in both files.
* Add the new library or package to the ``autodoc_mock_imports`` *list* in *ROOT/docs/conf.py*.
* Update the `version number <https://www.python.org/dev/peps/pep-0440/>`_ according to the `CONTRIBUTING <https://github.com/Ecohydraulics/flusstools-pckg/blob/main/docs/CONTRIBUTING.md>`_ standards.

Please use *PEP 8* for any code (read more on `hydro-informatics.github.io/hypy_pystyle <https://hydro-informatics.github.io/hypy_pystyle.html>`_) and try to keep the number of lines per script below 150 (it's hard or even apparently impossible sometimes - just try please).

To learn more about Python coding in general, visit the teaching website from the hydro-morphodynamics research group of the IWS: `hydro-informatics.github.io`_.


Download and Upload Project Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start with downloading (i.e., **pull** or **clone**) the project repository to your local computer.

.. admonition:: Windows Users

    Download and install `Git Bash <https://git-scm.com/downloads>`_. Linux users will most likely not need to install git because it is inherently part of the system tools.

Then open ``Git Bash`` (on Windows) or ``Terminal`` (on Linux or MacOS) and tap (replace capital letters with your target directory):

.. code-block::

    cd TARGET/DIRECTORY/
    git clone https://github.com/sschwindt/econnect.git
    cd econnect

Now, the source code for this website and the above shown ``example-solver.py`` script are copied to your local computer. To make changes in the code or to modify any existing file, you will need to become a contributor of this repository and you will need to `email Sebastian`_ to get the required read & write rights. Once you are a contributor, edit, add, or remove scripts and files in your local ``TARGET/DIRECTORY/econnect/`` (corresponds to ``ROOT``) folder. Consider to create a new subfolder in ``ROOT/codes/`` and save your code there locally (basically in any programming language). Then, upload, or **push** new code:

.. code-block::

    git add .
    git commit -m "ADD AN ACTIVE-VOICED MESSAGE IN SIMPLE PAST"
    git pull --rebase
    git push


If you encounter an error or warning after running ``git pull --rebase``, that means someone else has been editing the file at the same time. No worry about that, git will guide you through troubleshooting: Just open the concerned file and manually fix the indicated code blocks (indicator: ``<<<``  and ``>>>`` signs). Then follow the commands that *GitBash* or *Terminal* suggest you to use. To read more about git, visit `https://hydro-informatics.github.io/hy_git.html`.

.. important::

    Only push debugged code - Thank you!


.. admonition:: What is the goal of this approach?

    Using git enables version control and collaborative development of algorithms. Following coding standards (e.g., PEP8 styles), and with the help of git, the project results will be transparent, re-usable, safely stored, and accessible for anyone interested. Eventually, we want to provide the project results as a `pip-hosted <https://pypi.org/project/pip/>`_ Python package to leverage universal use of the project achievements along with coherent and understandable documentation.


How the Code Docs work
~~~~~~~~~~~~~~~~~~~~~~~

The automated code documentation of Sphinx ReadTheDocs automatically parses functions and classes for `docstrings <https://www.python.org/dev/peps/pep-0257/>`_ and implements them in the documentation. Python code docs are implemented via `google style <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_ of `docstrings in scripts <https://hydro-informatics.github.io/hypy_pystyle.html#docstrings>`_. Please familiarize with the style format and strictly apply in all commits.

To implement code documentations:

1. Save the file in ``ROOT/codes/`` (example: ``ROOT/codes/example_solver.py``).
2. Add a new section (create a new ``~~~`` header for single scripts/modules and a ``===`` header for new packages).
3. In the new header add the following:

.. code-block::

    .. automodule:: script-name (without.py at the end)
        :members:


Example
~~~~~~~

.. automodule:: example_solver
    :members:

More about Sphinx & ReadTheDocs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This page uses *Sphinx* `readthedocs <https://readthedocs.org/>`_ and the documentation regenerates automatically after pushing changes to the repositories ``main`` branch.

To set styles, configure or add extensions to the documentation use ``ROOT/.readthedocs.yml`` and ``ROOT/docs/conf.py``.

To modify this documentation file, edit ``ROOT/docs/index.rst`` (uses `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ format).

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


.. _email Sebastian: https://www.iws.uni-stuttgart.de/institut/team/Schwindt/
.. _hydro-informatics.github.io: https://hydro-informatics.github.io/