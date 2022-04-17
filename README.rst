===============================================================================
The Catalyst Python Template Repo
===============================================================================

.. readme-intro

.. image:: <https://www.repostatus.org/badges/latest/concept.svg>
   :target: <https://www.repostatus.org/#concept>
   :alt: Project Status: Concept - Minimal or no implementation has been done yet, or the repository is only intended to be a limited example, demo, or proof-of-concept.

.. image:: <https://github.com/catalyst-cooperative/python-template/workflows/tox-pytest/badge.svg>
   :target: <https://github.com/catalyst-cooperative/python-template/actions?query=workflow%3Atox-pytest>
   :alt: Tox-PyTest Status

#.. image:: <https://img.shields.io/readthedocs/package_name>
#   :target: <https://package_name.readthedocs.io/en/latest/>
#   :alt: Read the Docs Build Status

.. image:: <https://img.shields.io/codecov/c/github/catalyst-cooperative/python-template>
   :target: <https://codecov.io/gh/catalyst-cooperative/python-template>
   :alt: Codecov Test Coverage

#.. image:: <https://img.shields.io/pypi/v/catalystcoop.pudl>
#   :target: <https://pypi.org/project/catalystcoop.pudl/>
#   :alt: PyPI Latest Version

#.. image:: <https://img.shields.io/conda/vn/conda-forge/catalystcoop.pudl>
#   :target: <https://anaconda.org/conda-forge/catalystcoop.pudl>
#   :alt: conda-forge Version

#.. image:: <https://img.shields.io/pypi/pyversions/catalystcoop.pudl>
#   :target: <https://pypi.org/project/catalystcoop.pudl/>
#   :alt: Supported Python Versions

.. image:: <https://img.shields.io/badge/code%20style-black-000000.svg>
   :target: <https://github.com/psf/black>
   :alt: Any color you want, so long as it's black.

#.. image:: <https://zenodo.org/badge/80646423.svg>
#   :target: <https://zenodo.org/badge/latestdoi/80646423>
#   :alt: Zenodo DOI

A repository template to make setting up new Python projects easier and more uniform.

Remaining Tasks
---------------

* instructions in README for getting required tokens
* Change README to use RST
* instructions to run pre-commit install
* Add template cli.py module and entrypoint in setup.py
* Add template dostuff.py module called by cli.py

Python Packaging
----------------

* Use ``README.rst`` contents for the long description
* Default to MIT license
* Create ``dev``, ``docs```, and ``tests`` "extras" with packages required for linting,
  building the documentation with Sphinx, and running pytest using Sphinx.
* Use ``setuptools_scm`` to read package version from tags in GitHub.
* Include some default PyPI classifiers, assuming Python 3 support only.
* Use the `src` directory convention to avoid accidental package imports.

``pyproject.toml``
^^^^^^^^^^^^^^^^^^

* Use ``setuptools``, ``pip``, and ``wheel`` to manage package build.
* Use ``setuptools_scm`` for versioning.
* Configure ``black`` and ``isort`` to be compatible with each other.

Testing
-------

pytest
^^^^^^

Tox
^^^

* Set up code and documentation linters (`pre-commit`, `bandit`, `flake8`, `doc8`)
* Set up `unit` and `integration` test environments
* Build documentation using Sphinx.
* Generate cumulative coverage in the default `ci` testenv
* Configure basic PyPI release mechanics.
* Configure `flake8`, `doc8` and `pytest` to work with Google docstrings and `black`
  autoformatting.
* Store Tox virtual environment under ``.env_tox``

PyTest
-------

* Create a template ``tests/conftest.py``
* ``tests/unit`` and ``tests/integration`` test directories
* stub ``__init__.py`` files to make it all usable by ``pytest``

Documentation
-------------

* Create a template ``docs/conf.py``
* Automatically include: ``README.rst``, ``LICENSE.txt``, ``CODE_OF_CONDUCT.rst``
* Build API documentation with ``AutoAPI``
* Configure ReadTheDocs builds

Git Pre-commit Hooks
--------------------

* What do the pre-commit hooks do?
* How do you install them?

Licensing
---------

In general, our code, data, and other work are permissively licensed for use by
anybody, for any purpose, so long as you give us credit for the work we've done.

* For software we use `the MIT License <https://opensource.org/licenses/MIT>`__.
* For data, documentation, and other non-software works we use the
  `CC-BY-4.0 <https://creativecommons.org/licenses/by/4.0/>`__

Contact Us
----------

* For general support, questions, or other conversations around the project
  that might be of interest to others, check out the
  `GitHub Discussions <https://github.com/catalyst-cooperative/pudl/discussions>`__
* If you'd like to get occasional updates about our projects
  `sign up for our email list <https://catalyst.coop/updates/>`__.
* Want to schedule a time to chat with us one-on-one? Join us for
  `Office Hours <https://calend.ly/catalyst-cooperative/pudl-office-hours>`__
* Follow us on Twitter: `@CatalystCoop <https://twitter.com/CatalystCoop>`__
* More info on our website: https://catalyst.coop
* For private communication about the project or to hire us to provide customized data
  extraction and analysis, you can email the maintainers:
  `pudl@catalyst.coop <mailto:pudl@catalyst.coop>`__

About Catalyst Cooperative
--------------------------

`Catalyst Cooperative <https://catalyst.coop>`__ is a small group of data
wranglers and policy wonks organized as a worker-owned cooperative consultancy.
Our goal is a more just, livable, and sustainable world. We integrate public
data and perform custom analyses to inform public policy (`Hire us!
<https://catalyst.coop/hire-catalyst>`__). Our focus is primarily on mitigating
climate change and improving electric utility regulation in the United States.
