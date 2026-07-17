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

### Python Package Skeleton

- The `src` directory contains the code that will be packaged and deployed on the user
    system. That code is in a directory with the same name as the package.
- Using a separate `src` directory helps avoid accidentally importing the package when
    you're working in the top level directory of the repository.
- A simple python module (`dummy.py`), and a separate module providing a command line
    interface to that module (`cli.py`) are included as examples.
- Any files in the `src/package_data/` directory will also be packaged and deployed.
- What files are included in or excluded from the package on the user's system is
    controlled by the `[tool.hatch.build.targets.wheel]` options in `pyproject.toml`.
    We build with [hatchling](https://hatch.pypa.io/latest/), which packages every file
    under the specified `packages` directory (both `.py` and non-Python files) --
    there's no separate `MANIFEST.in` to maintain.
- The CLI is deployed using `project.scripts` defined in `pyproject.toml`.
- We use [hatch-vcs](https://github.com/ofek/hatch-vcs) (configured under
    `[tool.hatch.version]`) to obtain the package's version directly from `git` tags,
    rather than storing it in the repository and manually updating it.
- `README.md` is read in and used for the package's `long_description`. This is what is
    displayed on the PyPI page for the package.
- By default we create several sets of "extras" -- additional optional package
    dependencies that can be installed in special circumstances: `dev`, `docs`, `lint`,
    `tests`, and `types`. The packages listed there are used in development, building the
    docs, linting, running the tests, and type checking (respectively) but aren't
    required for a normal user who is just installing the package from `pip` or `conda`.
    These are defined under the `project.optional-dependencies` section of
    `pyproject.toml`.

### Environment & Task Management with Pixi

- We use [pixi](https://pixi.sh) to manage the development environment and the tasks
    used to test, lint, format, and document the project.
- Run `pixi install` once to create the environment described in `pyproject.toml`
    (under `[tool.pixi.*]`), then use `pixi run <task>` to run any of the tasks defined
    under `[tool.pixi.tasks]`.
- The most important tasks are:
    - `pixi run test` -- run all the unit and integration tests under `tests/` with
        pytest and report test coverage.
    - `pixi run lint` -- run `ruff` and `pyrefly` to catch errors and style issues.
    - `pixi run format` -- automatically reformat the code and other files using `ruff`,
        `taplo`, `mdformat`, and `prettier`.
    - `pixi run docs` -- build the documentation with `zensical`.
- There's a single `default` pixi environment that contains everything needed for
    local development, since splitting a small template repository into many
    environments adds more complexity than it saves.
- This package is installed into that environment in editable mode via
    `[tool.pixi.pypi-dependencies]`, which explicitly lists every extra from
    `project.optional-dependencies` (`dev`, `docs`, `lint`, `tests`, `types`) that
    should be pulled in, rather than relying on pixi's implicit behavior of matching
    same-named pixi features to extras. The one named pixi feature that still exists,
    `lint`, exists only to add a few non-Python formatting tools (`taplo`, `prettier`,
    `mdformat`, etc.) that aren't published to PyPI and so can't be expressed as an
    extra.

### Devcontainer

- `.devcontainer/devcontainer.json` defines a basic, editor-agnostic
    [development container](https://containers.dev/): the same `ghcr.io/prefix-dev/pixi`
    image used in `docker/Dockerfile`, with `git` added (the base image doesn't include
    it, and `pixi install` needs it to derive the package version from `git` tags) and
    `pixi install` / `pixi run prek install` run automatically once the container
    starts. It works with VS Code, JetBrains Gateway, GitHub Codespaces, or the
    standalone [devcontainer CLI](https://github.com/devcontainers/cli) -- useful for
    giving a coding agent (or a human) an isolated, reproducible, disposable sandbox to
    work in instead of your host machine.

### Pytest Testing Framework

- A skeleton [pytest](https://docs.pytest.org/) testing setup is included in the
    `tests/` directory.
- Tests are split into `unit` and `integration` categories.
- Session-wide test fixtures, additional command line options, and other pytest
    configuration can be added to `tests/conftest.py`.
- Exactly what pytest commands are run during continuous integration is controlled by
    the pixi tasks defined in `pyproject.toml`.
- Pytest can also be run manually without going through pixi, but will use whatever
    your personal python environment happens to be, rather than the one specified by the
    package. Running pytest on its own is a good way to debug new or failing tests
    quickly, but we should always use `pixi run test` for actual testing.

### Git Pre-commit Hooks

- A variety of sanity checks are defined as git pre-commit hooks -- they run any time
    you try to make a commit, to catch common issues before they are saved. Many of these
    hooks are taken from the excellent [pre-commit project](https://pre-commit.com/).
- The hooks are configured in `.pre-commit-config.yaml`, and run using
    [prek](https://prek.j178.dev/), a much faster, dependency-free tool that reads that
    same standard config format.
- For them to run automatically when you try to make a commit, you **must** install
    the hooks in your cloned repository first by running `pixi run prek install`. This
    only has to be done once.
- These checks are run as part of our CI, and the CI will fail if the hooks fail.
- We also use the [pre-commit.ci](https://pre-commit.ci) service to run the same
    checks on any code that is pushed to GitHub, and to apply standard code formatting
    to the PR in case it hasn't been run locally prior to being committed.
- Run `pixi run prek-update` to bump the hook `rev` pins in `.pre-commit-config.yaml`
    to their latest versions. The `update-lockfiles` GitHub Action runs this (along
    with `pixi update` for `pixi.lock`) weekly and opens a PR with the changes.

### Code Formatting & Linting

To avoid the tedium of meticulously formatting all the code ourselves, and to ensure a
standard style of formatting and syntactical idioms across the codebase, we use the
`ruff` code linter and formatter, which runs both as a pre-commit hook and via
`pixi run format` / `pixi run lint`. These can be integrated directly into your text
editor or IDE with the appropriate plugins. The `ruff` linter / formatter has a huge
array of configuration options and different kinds of checks it can run, which are
defined under the `tool.ruff` section of `pyproject.toml`.

We also have a custom hook that clears Jupyter notebook outputs prior to committing.

### Type Checking

We use [pyrefly](https://pyrefly.org/), a fast Rust-based type checker. It's
configured under the `tool.pyrefly` section of `pyproject.toml` and run via
`pixi run lint`.

### Code & Documentation Linters

To catch errors before commits are made, and to ensure uniform formatting across the
codebase, we also use linters outside of `ruff`. They don't change the code or
documentation files, but they will raise an error or warning when something doesn't
look right so you can fix it.

- `pre-commit` has a collection of built-in checks that
    [use pygrep to search Python files](https://github.com/pre-commit/pygrep-hooks) for
    common problems, as well as
    [language agnostic problems](https://github.com/pre-commit/pre-commit-hooks) like
    accidentally checking large binary files into the repository or having unresolved
    merge conflicts.
- [hadolint](https://github.com/AleksaC/hadolint-py) checks Dockerfiles for errors and
    violations of best practices. It runs as a pre-commit hook.
- [actionlint](https://github.com/rhysd/actionlint) checks the GitHub Actions workflow
    files for errors. It runs as a pre-commit hook.
- [markdownlint](https://github.com/DavidAnson/markdownlint) and
    [mdformat](https://mdformat.readthedocs.io/) check and reformat the Markdown
    documentation. The `mdformat-mkdocs` plugin keeps `mdformat` from mangling
    Zensical/MkDocs-flavored syntax, like the snippet-include lines mentioned above.

### Test Coverage

- We use the pytest `coverage` plugin to measure and record what percentage of our
    codebase is being tested, and to identify which modules, functions, and individual
    lines of code are not being exercised by the tests.
- When you run `pixi run test`, a summary of the test coverage will be printed at the
    end of the tests (assuming they succeed). The full details of the test coverage are
    written to `coverage.xml`.
- There are some configuration options for this process set in the
    `tool.coverage.report` section of `pyproject.toml`.
- When the tests are run via the `pytest` workflow in GitHub Actions, the test coverage
    data from the `coverage.xml` output is uploaded to a service called
    [CodeCov](https://about.codecov.io/) that saves historical data about our test
    coverage, and provides a nice visual representation of the data -- identifying which
    subpackages, modules, and individual lines are being tested. For example, here are
    the results
    [for the cheshire repo](https://app.codecov.io/gh/catalyst-cooperative/cheshire).
- The connection to CodeCov is configured in the `.codecov.yml` YAML file. Uploads
    authenticate with the `catalyst-cooperative` org's shared "Global Upload Token,"
    stored as an organization-level `CODECOV_TOKEN` secret in GitHub, so individual
    repos don't need their own CodeCov token minted and stored separately.
- CodeCov also adds a couple of test coverage checks to any pull request, to alert us
    if a PR reduces overall test coverage (which we would like to avoid).

### Documentation Builds

- We build our documentation using [Zensical](https://zensical.org/), a modern
    Markdown-based static site generator from the Material for MkDocs team.
- Standalone docs files are stored under the `docs/` directory as Markdown, and the
    Zensical configuration lives in `zensical.toml` at the top of the repository.
- The top level documentation page (`docs/index.md`) simply embeds this `README.md`
    verbatim using Zensical's `pymdownx.snippets` syntax (`--8<-- "README.md"`);
    `docs/license.md` embeds `LICENSE.txt` the same way. `docs/code_of_conduct.md` and
    `docs/release_notes.md` are standalone Markdown files.
- `docs/reference.md` holds the API reference, rendered from docstrings by
    [mkdocstrings](https://mkdocstrings.github.io/) (configured under
    `[project.plugins.mkdocstrings...]` in `zensical.toml`, currently a preliminary
    Zensical integration). Add a `::: module.path` line there for any new module that
    should show up in the API reference -- it isn't generated automatically.
- Build the docs with `pixi run docs`, which wipes the previously generated `site/`
    directory and rebuilds everything from scratch, or preview them locally with
    `pixi run docs-serve`.

### Documentation Publishing

- We publish our documentation to [GitHub Pages](https://pages.github.com/).
- When you push to `main` the `docs` GitHub Actions workflow builds the site with
    Zensical and deploys it automatically.
- To enable this for a new repository, go to the repo's Settings -> Pages, and under
    "Build and deployment" set the source to "GitHub Actions."

### Dependabot

We use GitHub's
[Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates)
to automatically update the versions of the
[GitHub Actions](https://docs.github.com/en/actions) that we employ, configured in
`.github/dependabot.yml`. Our Python dependencies are refreshed separately, by the
weekly `update-lockfiles` GitHub Action described below, instead of by Dependabot.

### GitHub Actions

Under `.github/workflows` are YAML files that configure the
[GitHub Actions](https://docs.github.com/en/actions) associated with the repository.
We use GitHub Actions to:

- Run continuous integration with `pixi run test` and upload test coverage to
    CodeCov.
- Build the documentation with Zensical and deploy it to GitHub Pages.
- Build a Docker container using the
    [docker-build-push action](https://github.com/docker/build-push-action) for every
    commit and PR, once `pytest` has passed for it, to catch `Dockerfile` breakage
    early. It's only pushed to Docker Hub for `main` and version tags, so branches and
    PRs don't clutter the registry with images nobody will pull.
- Release a new version of the package on PyPI when a version tag is pushed to `main`.
- Approve and enable auto-merge on bot PRs from pre-commit.ci and Dependabot, using
    `gh pr merge --auto`, which respects our merge queue and required status checks.
- Refresh `pixi.lock` and the `rev` pins in `.pre-commit-config.yaml` weekly, opening
    a PR with the changes so CI can confirm the updated dependencies still work.

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
