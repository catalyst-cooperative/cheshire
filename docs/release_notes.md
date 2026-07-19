# PACKAGE_NAME Release Notes

## X.Y.Z (YYYY-MM-DD)

<!-- Copy this section to the top of the file for each new release: fill in the real
version number and date above, and delete whichever subheadings below don't apply.

Agents: don't fill in real content here -- this is a reusable template, not a place to
record actual changes. Add your change to the section for the upcoming/unreleased
version instead: that's the first real, numbered `## X.Y.Z (YYYY-MM-DD)` section below
this one. If it doesn't exist yet, create it (with a placeholder date, or the expected
release date if known) by copying this template immediately below it, same as you
would when cutting an actual release. See AGENTS.md's Documentation section for more. -->

### What's New?

- Briefly describe the substantial changes to the code in here when you make a PR.
- That way users (and future us) have documentation as to what's going on.
- You can refer to the relevant pull request like this: !1
- Don't hesitate to give shoutouts to folks who contributed, e.g. @cmgosnell
- You can link to issues that were closed like this: #2, #3, #4

### Bug Fixes

- It's good to make a note of any known bugs that are fixed by the release, and refer
    to the relevant issues.

### Known Issues

- It's also good to list any remaining known problems, and link to their issues too.

## 0.5.8 (2026-07-19)

### What's New?

- Every task under `[tool.pixi.tasks]` in `pyproject.toml` now has a `description`,
    so `pixi task list` (and the description pixi prints alongside each task as it
    runs) actually explains what each one does, instead of leaving the `Description`
    column blank. See PR !547
- Replaced references to installing packages with `pip` in `README.md` and
    `docs/tools.md` with [uv](https://docs.astral.sh/uv/), which is faster and has
    become the de facto standard. Left two references to `pip` alone where switching
    wouldn't make sense: `docs/release_notes.md`'s historical changelog entries (which
    describe a past Dependabot config value, not an instruction to users) and the
    transient `pip install setuptools-scm` step in `docker-build-push.yml` (a single
    lightweight package installed once on an ephemeral CI runner, where `uv`'s speed
    advantage isn't worth the extra `setup-uv` action). See PR !547
- Added [typos](https://github.com/crate-ci/typos) (via the
    `adhtruong/mirrors-typos` pre-commit hook) to spell check documentation and code
    comments, and [detect-secrets](https://github.com/Yelp/detect-secrets) to scan
    for accidentally committed secrets and credentials, with a fresh `.secrets.baseline`
    recording that nothing was found. Both run as regular pre-commit.ci-hosted hooks,
    same as `markdownlint-cli2`/`shellcheck`/`actionlint`, so they don't need a
    dedicated pixi task or CI step. See PR !547
- Marked `pixi.lock` `merge=ours` in `.gitattributes`, so a merge conflict on the
    generated lockfile keeps our side instead of attempting a line-by-line merge --
    `pixi install`/`pixi update` regenerates it anyway, so a hand-merged version would
    just be replaced. Also marked `*.ipynb` `linguist-detectable=false`, so notebook
    JSON doesn't dominate GitHub's per-repo language statistics. **`merge=ours` needs
    a one-time, per-clone `git config merge.ours.driver true` to actually take
    effect** -- git silently ignores the attribute otherwise, by design, since a
    tracked file can't be allowed to specify an arbitrary merge driver to run without
    each clone opting in locally first. Existing clones should run that command once
    to pick this up. See PR !547
- Documented all of the above in `docs/tools.md`: added `typos`/`detect-secrets` to
    the "Code & Documentation Linters" list, and added a new "Git Attributes" section
    (linked from `README.md`) covering `.gitattributes` and the `merge.ours.driver`
    setup step. See PR !547

## 0.5.7 (2026-07-18)

### What's New?

- Replaced [pyrefly](https://pyrefly.org/) with [ty](https://github.com/astral-sh/ty)
    (Astral's Rust-based type checker) for type checking, configured under the new
    `[tool.ty.src]`/`[tool.ty.environment]` sections of `pyproject.toml` and run via
    `pixi run lint`. Unlike pyrefly's official pre-commit hook, ty's official hook
    shells out to `uv check`, which needs network access to resolve dependencies --
    incompatible with pre-commit.ci. It now runs as a local pre-commit hook through
    the pixi environment instead, and is separately enforced by a dedicated step in
    the `pytest` GitHub Actions workflow, since pre-commit.ci skips it. See PR !544
- Added a `.gitattributes` file marking `pixi.lock` as `linguist-generated`, so
    GitHub collapses it by default in PR diffs instead of it dominating the review
    every time a dependency changes. See PR !544

### Bug Fixes

- Narrowed the GitHub App token used by `update-lockfiles.yml` to just the
    `contents`/`pull-requests` permissions that workflow actually needs, instead of
    inheriting the app's full installed permission set, and stopped `actions/checkout`
    from persisting that token in the local git config once nothing after checkout
    needs it. See PR !544

## 0.5.6 (2026-07-17)

### Bug Fixes

- Fixed the `build-package-release` workflow's pre-release check, which only
    verified the tagged commit was an *ancestor* of `main` -- true of any past commit
    on `main`, including a stale local `main` that's behind `origin`. It now requires
    an exact match against `origin/main`'s current tip, so tagging from a stale local
    checkout fails loudly instead of silently releasing an old commit.

## 0.5.5 (2026-07-17)

No functional changes. This tag points at the same commit as `v0.5.4` -- another
instance of the same stale-tag pattern `0.5.6`, above, now catches.

## 0.5.4 (2026-07-17)

### What's New?

- Moved the "What this template provides" tooling documentation out of `README.md`
    and into a new `docs/tools.md` page, linked from a short list in the README, so
    the README stays focused on getting started and the docs site carries the
    in-depth tooling reference.
- Added the [shellcheck](https://github.com/shellcheck-py/shellcheck-py) pre-commit
    hook to catch common bugs and portability issues in any shell scripts added to the
    repo.
- Renamed the local `unit-tests` pre-commit hook to `pytest` for clarity.

### Bug Fixes

- Fixed `test_winston_args` in `tests/integration/console_scripts_test.py`, which was
    marking non-integer CLI arguments as `xfail` even though rejecting them is the
    correct, intended behavior. Split it into `test_winston_valid_args` and
    `test_winston_invalid_args`, with the latter asserting the expected failure
    (non-zero exit code and an "invalid int value" error) so it reports a real PASS
    instead of masking the backwards assertion with `xfail`.
- Removed a stale link to PUDL's release notes page from the PR template's
    documentation checklist; it now just says to update the release notes.

## 0.5.3 (2026-07-17)

No functional changes. This tag points at the same commit as `v0.5.2` -- consistent
with being cut from a stale local `main`, the exact failure mode `0.5.5`, above, now
catches.

## 0.5.2 (2026-07-17)

### What's New?

- Added basic `.github/ISSUE_TEMPLATE/task.md` and `.github/pull_request_template.md`
    templates (!540).
- Excluded `dependabot[bot]` and `pre-commit-ci[bot]` authored PRs from GitHub's
    auto-generated release notes, via a new `.github/release.yml`, so only
    substantive PRs show up there (!541).

### Bug Fixes

- Disabled `markdownlint`'s `MD025` front-matter-title heuristic, which was flagging
    a false "multiple top-level headings" error on `title:` keys in GitHub issue
    template front matter.
- Added the `mdformat-frontmatter` plugin so `mdformat` recognizes YAML front matter
    (used by the new issue/PR templates) instead of mangling its `---` delimiters into
    thematic breaks.

## 0.5.1 (2026-07-17)

### What's New?

- Replaced the archived `tibdex/github-app-token` action with the official
    `actions/create-github-app-token`, and replaced `ridedott/merge-me-action` with
    `gh pr merge --auto`, which is documented to be merge-queue-aware.
- Switched `bot-auto-merge` to trigger on `pull_request_target` (restricted to the
    `dependabot`/`pre-commit-ci` actors) instead of `workflow_run`.
- Grouped all `github-actions` ecosystem Dependabot updates into a single PR, and
    dropped the `pip` ecosystem entry (Python dependencies are refreshed weekly by
    `update-lockfiles.yml` instead).
- Added `.devcontainer/devcontainer.json`, a basic editor-agnostic
    [development container](https://containers.dev/).
- Pointed the docs badge/links at the intended `docs.catalyst.coop/cheshire` URL, and
    added real social links (BlueSky, Mastodon, LinkedIn, Open Collective) to the docs
    footer.
- Enabled `pymdownx.magiclink` shorthand (`#123`, `@user`, etc. auto-link to GitHub).

### Bug Fixes

- Switched CodeCov uploads to the org's shared "Global Upload Token" instead of a
    stale hardcoded per-repo token, and stopped coverage-upload failures from failing
    the required `pytest` check. (!537)

## 0.5.0 (2026-07-16)

### What's New?

- Major modernization overhaul of the template's tooling:
    - Replaced tox + conda with [pixi](https://pixi.sh) for environment and task
        management (`pixi run test`, `lint`, `format`, `docs`, `build`).
    - Replaced Sphinx/RST docs with [Zensical](https://zensical.org/) and Markdown,
        including an API reference page rendered by `mkdocstrings`.
    - Replaced `setuptools`/`setuptools_scm` with `hatchling`/`hatch-vcs`, so the
        version still comes straight from git tags.
    - Replaced `mypy` with [pyrefly](https://pyrefly.org/) for type checking.
    - Switched from running `pre-commit` directly to running the same
        `.pre-commit-config.yaml` via [prek](https://prek.j178.dev/), and added several
        new hooks (`trailing-whitespace`, `detect-private-key`, `destroyed-symlinks`,
        `check-json`, `no-commit-to-branch`, a few more `pygrep-hooks`, and
        `mdformat-mkdocs`).
    - Rewrote the GitHub Actions workflows: CI now runs through pixi (`pytest.yml`),
        docs are built and published to GitHub Pages (`docs.yml`), Docker images are
        only pushed for `main`/tags and only once tests pass (`docker-build-push.yml`),
        and a new weekly `update-lockfiles.yml` refreshes `pixi.lock` and the
        pre-commit hook pins.
    - Converted `README.rst` to `README.md`, and added a template `AGENTS.md`
        (symlinked from `CLAUDE.md`) with instructions for AI coding agents.
    - Removed a pile of now-dead tooling and cruft: `tox.ini`, `environment.yml`,
        `.readthedocs.yml`, `.coveragerc`, `MANIFEST.in`.
    - Removed upper version bounds from our dependencies, relying on `pixi.lock` for
        reproducibility instead.

### Known Issues

- Zensical and its `mkdocstrings` integration are both still pre-1.0 and may change.
- Automatic API reference generation (e.g. via `mkdocs-gen-files`) isn't supported by
    Zensical yet, so `docs/reference.md` has to be updated by hand for new modules.

## 0.4.1 (2023-09-17)

### What's New?

- Adopt `ruff` for linting.

## 0.4.0 (2023-09-16)

### What's New?

- Publish releases to real PyPI instead of TestPyPI.
- Notify Slack when a new release is published.
- Remove the old `repo2docker` workflow.

## 0.3.4 (2023-09-15)

### What's New?

- Remove the obsolete `setup.py`; rely solely on `pyproject.toml`.

## 0.3.3 (2023-09-15)

### What's New?

- Auto-generate GitHub release notes from merged PRs.

## 0.3.2 (2023-09-15)

### What's New?

- Use `gh release create` instead of manually uploading release assets.

## 0.3.1 (2023-09-15)

### What's New?

- Pin the Sigstore signing action to an exact version for reliable release signing.

## 0.3.0 (2023-09-15)

### What's New?

- Release process housekeeping; no user-facing changes.

## 0.2.1 (2023-09-15)

### Bug Fixes

- Fix the documentation deployment environment URL.

## 0.2.0 (2023-09-15)

### What's New?

- Add a `Dockerfile`, `hadolint` linting, and the `docker-build-push` workflow.
- Migrate to `rstcheck` 6.0.
- Consolidate the CI, notification, and dependabot-merge jobs into distinct
    workflows.

## 0.1.0 (2022-04-29)

### What's New?

- This is the first fully functional and documented version of our template repository.

### Known Issues

- Need to get some user feedback!
- Still need to look at updating our Code of Conduct. See #12
