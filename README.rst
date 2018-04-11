=======================
Template python project
=======================

.. image:: https://travis-ci.org/apolopeix/template-python-project.svg?branch=master
    :target: http://travis-ci.org/apolopeix/template-python-project
    :alt: Build Status
.. image:: https://travis-ci.org/apolopeix/template-python-project/coverage.svg?branch=master
    :target: https://codecov.io/gh/apolopeix/template-python-project?branch=master
    :alt: Code Coverage

This project is a template that can be used to quickly start new python projects.

Features
========

- Initial project layout
- Basic test infrastructure
- Easy Travis CI integration using
  - Pytest
  - Code coverage
  - Setup tools


Build project locally
=====================

Requires python3 to run with support for virtualenvs:

.. code-block:: bash

    python3 -m venv .venv_template-python-project
    source .venv_template-python-project/bin/activate
    pip3 install tox
    tox
