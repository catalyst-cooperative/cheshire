# Cheshire: a Python Template Repository for Catalyst

<!-- readme-intro -->

[![pytest](https://github.com/catalyst-cooperative/cheshire/actions/workflows/pytest.yml/badge.svg)](https://github.com/catalyst-cooperative/cheshire/actions/workflows/pytest.yml)
[![docker-build-push](https://github.com/catalyst-cooperative/cheshire/actions/workflows/docker-build-push.yml/badge.svg)](https://github.com/catalyst-cooperative/cheshire/actions/workflows/docker-build-push.yml)
[![Codecov Test Coverage](https://img.shields.io/codecov/c/github/catalyst-cooperative/cheshire?style=flat&logo=codecov)](https://codecov.io/gh/catalyst-cooperative/cheshire)
[![Documentation](https://img.shields.io/github/deployments/catalyst-cooperative/cheshire/github-pages?style=flat&logo=githubpages&label=docs)](https://docs.catalyst.coop/cheshire)
[![PyPI Latest Version](https://img.shields.io/pypi/v/catalystcoop.cheshire?style=flat&logo=python)](https://pypi.org/project/catalystcoop.cheshire/)
[![conda-forge Version](https://img.shields.io/conda/vn/conda-forge/catalystcoop.cheshire?style=flat&logo=condaforge)](https://anaconda.org/conda-forge/catalystcoop.cheshire)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/catalystcoop.cheshire?style=flat&logo=python)](https://pypi.org/project/catalystcoop.cheshire/)

This template repository helps make new Python projects easier to set up and more
uniform. It contains a lot of infrastructure surrounding a minimal Python package named
`cheshire` (the cat who isn't entirely there...).

## Create a new repository from this template

- Choose a name for the new package that you are creating.
- The name of the repository should be the same as the name of the new Python package
    you are going to create. E.g. a repository at `catalyst-cooperative/cheshire` should
    be used to define a package named `cheshire`.
- Fork this template repository to create a new Python project repo.
    [See these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
- Clone the new repository to your development machine.
- Install [pixi](https://pixi.sh) if you don't already have it.
- Run `pixi run prek install` in the newly cloned repository to install the
    [pre-commit hooks](https://pre-commit.com/) defined in `.pre-commit-config.yaml`,
    using [prek](https://prek.j178.dev/) as the runner.
- Run `pixi run test` from the top level of the repository to verify that everything
    is working correctly.

## Rename the package and distribution

Once you know that your forked version of the `cheshire` package is working as
expected, you should update the package and distribution names in your new repo to
reflect the name of your new package. The **package name** is determined by the name of
the directory under `src/` which contains the source code, and is the name you'll use
to import the package for use in a program, script, or notebook. E.g.:

```python
import cheshire
```

The **distribution name** is the name that is used to install the software using a
program like `pip`, `conda`, or `pixi`. It is often identical to the package name, but
can also contain a prefix namespace that indicates the individual or organization
responsible for maintaining the package. See
[PEP 423](https://peps.python.org/pep-0423/) for more on Python package naming
conventions. We are using the `catalystcoop` namespace for the packages that we
publish, so our `pudl` package becomes `catalystcoop.pudl` in the Python Package Index
(PyPI) or on `conda-forge`. Similarly the `cheshire` package becomes the
`catalystcoop.cheshire` distribution. The distribution name is determined by the
`project.name` defined in `pyproject.toml`.

```bash
pip install catalystcoop.cheshire
```

The package and distribution names are referenced in many of the files in the template
repository, and they all need to be replaced with the name of your new package. You can
use `grep -r` to search recursively through all of the files for the word `cheshire`
at the command line, or use the search-and-replace functionality of your IDE / text
editor. The name of the package directory under `src/` will also need to be changed.

- Supply any required tokens, e.g. for CodeCov.
- Rename the `src/cheshire` directory to reflect the new package name.
- Search for `cheshire` and replace it as appropriate everywhere. Sometimes this will
    be with a distribution name like `catalystcoop.cheshire` (the package as it appears
    for `pip` or `PyPI`) and sometimes this will be the importable package name (the name
    of the directory under `src` e.g. `cheshire`).
- Enable GitHub Pages for the new repository (Settings -> Pages -> Source: GitHub
    Actions) so the `docs` workflow can publish the documentation.

## What this template provides

See [the Tooling docs](https://docs.catalyst.coop/cheshire/tools/) for details on all
of the tooling this template sets up:

- [Python Package Skeleton](https://docs.catalyst.coop/cheshire/tools/#python-package-skeleton)
- [Environment & Task Management with Pixi](https://docs.catalyst.coop/cheshire/tools/#environment-task-management-with-pixi)
- [Devcontainer](https://docs.catalyst.coop/cheshire/tools/#devcontainer)
- [Pytest Testing Framework](https://docs.catalyst.coop/cheshire/tools/#pytest-testing-framework)
- [Git Pre-commit Hooks](https://docs.catalyst.coop/cheshire/tools/#git-pre-commit-hooks)
- [Code Formatting & Linting](https://docs.catalyst.coop/cheshire/tools/#code-formatting-linting)
- [Type Checking](https://docs.catalyst.coop/cheshire/tools/#type-checking)
- [Code & Documentation Linters](https://docs.catalyst.coop/cheshire/tools/#code-documentation-linters)
- [Test Coverage](https://docs.catalyst.coop/cheshire/tools/#test-coverage)
- [Documentation Builds](https://docs.catalyst.coop/cheshire/tools/#documentation-builds)
- [Documentation Publishing](https://docs.catalyst.coop/cheshire/tools/#documentation-publishing)
- [Dependabot](https://docs.catalyst.coop/cheshire/tools/#dependabot)
- [GitHub Actions](https://docs.catalyst.coop/cheshire/tools/#github-actions)

## About Catalyst Cooperative

[Catalyst Cooperative](https://catalyst.coop) is a small group of data wranglers and
policy wonks organized as a worker-owned cooperative consultancy. Our goal is a more
just, livable, and sustainable world. We integrate public data and perform custom
analyses to inform public policy
([Hire us!](https://catalyst.coop/hire-catalyst)). Our focus is primarily on
mitigating climate change and improving electric utility regulation in the United
States.

### Contact Us

- For general support, questions, or other conversations around the project that
    might be of interest to others, check out the
    [GitHub Discussions](https://github.com/catalyst-cooperative/pudl/discussions).
- If you'd like to get occasional updates about our projects
    [sign up for our email list](https://catalyst.coop/updates/).
- Want to schedule a time to chat with us one-on-one? Join us for
    [Office Hours](https://calend.ly/catalyst-cooperative/pudl-office-hours).
- More info on our website: <https://catalyst.coop>
- For private communication about the project or to hire us to provide customized data
    extraction and analysis, you can email the maintainers:
    [pudl@catalyst.coop](mailto:pudl@catalyst.coop).
