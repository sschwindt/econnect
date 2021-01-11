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

.. admonition:: Large data sharing
    :what: Files larger than 100MB
    :how: bwSync&Share - `email Sebastian`_ for read & write access.

Instructions
============

Create new Code
~~~~~~~~~~~~~~~


.. sidebar:: A code example

    The Python script ``example_solver.py`` lives in the host repository of this website in ``ROOT/codes/``. The left column shows this Python script in its original form with docstrings (the ``"""This is a docstring"""``). To learn more about Python coding in general, visit the teaching website from the hydro-morphodynamics research group of the IWS: `hydro-informatics.github.io`_.

.. literalinclude:: example_solver.py
    :language: python
    :caption: ROOT/codes/example_solver.py
    :linenos:
    :lines: 1-30



Download and Upload Project Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start with downloading (i.e., **pull** or **clone**) the project repository to your local computer.

To upload, or **push** new code (in any programming language), consider to create a new subfolder in ``ROOT/codes/`` and save your code there locally.


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

.. _email Sebastian: https://www.iws.uni-stuttgart.de/institut/team/Schwindt/
.. _hydro-informatics.github.io: https://hydro-informatics.github.io/