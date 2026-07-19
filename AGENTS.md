# AGENTS.md

Instructions for AI coding agents (Claude Code, Cursor, Copilot, etc.) working in this
repository. This file is a template -- replace the bracketed `[...]` prompts with
specifics for your project, delete sections that don't apply, and add new ones as
needed. Keep it current: treat stale instructions here as a bug, since agents will
follow whatever this file says even after it stops being true.

## Project overview

<!--
One or two paragraphs. What does this package do, and who is it for? Agents use this
to decide what's in scope for a change and what would be a surprising, out-of-place
addition.

Example: "This package ingests XYZ data from the ABC public API, cleans and validates
it, and publishes normalized Parquet tables. It's a dependency of the main ETL
pipeline, not a standalone tool."
-->

[Replace this with a short description of the project.]

## Setup commands

This template uses [pixi](https://pixi.sh) to manage the development environment and
tasks, defined under `[tool.pixi.*]` in `pyproject.toml`.

- Install [pixi](https://pixi.sh/latest/installation/) if it isn't already available.
- Run `pixi install` once to create the `default` environment.
- Run `pixi run prek install` once to install the git pre-commit hooks (run via
    [prek](https://prek.j178.dev/), a fast drop-in replacement for `pre-commit` that
    still reads `.pre-commit-config.yaml`).
- Run `git config merge.ours.driver true` once so the `merge=ours` rule in
    `.gitattributes` actually takes effect on `pixi.lock` conflicts -- git ignores that
    attribute silently otherwise, since a repo-tracked file can't be allowed to specify
    an arbitrary merge driver to run without the clone opting in locally first.

<!--
If your project needs additional one-time setup -- database seeding, credentials,
downloading reference data, environment variables, Docker services, etc. -- document
the exact commands here. An agent can't infer steps that only exist in a teammate's
head or a wiki page.
-->

## Task commands

Run everything through pixi tasks rather than calling the underlying tools directly,
so agents use the same invocations CI does:

- `pixi run test` -- run the unit and integration tests under `tests/` with pytest,
    and report combined test coverage.
- `pixi run lint` -- run `ruff` and `ty` (static analysis and type checking). Doesn't
    modify files.
- `pixi run format` -- automatically reformat code and other files with `ruff`,
    `taplo`, `mdformat`, and `prettier`. Run this before committing.
- `pixi run docs` -- build the documentation with `zensical` into `site/`.
- `pixi run docs-serve` -- serve the documentation locally with live reload.
- `pixi run build` -- build the sdist/wheel and check them with `twine`.
- `pixi run prek-update` -- bump the hook `rev` pins in `.pre-commit-config.yaml` to
    their latest versions. Run automatically, alongside `pixi update` for
    `pixi.lock`, by the weekly `update-lockfiles` GitHub Action.

An agent should run `pixi run lint` and `pixi run test` before considering a change
complete, and `pixi run format` if it touched code, TOML, YAML, or Markdown files.

<!--
If you add pixi tasks that are specific to this project (e.g. running a local
service, regenerating fixtures, applying migrations), list them here with a one-line
description of what each one does and when to use it.
-->

## Code style

- Formatting and most style rules are enforced by `ruff` (see `[tool.ruff]` in
    `pyproject.toml`) and applied automatically by `pixi run format` / the `ruff` and
    `ruff-format` pre-commit hooks. Don't hand-format code to match a personal
    preference that conflicts with what `ruff format` produces.
- Type checking is done with `ty` (see `[tool.ty.src]`). New code should be typed;
    if you must suppress a false positive, use a `# ty: ignore[rule-name]` comment
    with a short note explaining *why* it's a false positive, not just that it is one.
- Docstrings use the Google convention (`[tool.ruff.lint.pydocstyle]`).

<!--
Add anything specific to this codebase that a generic Python style guide wouldn't
tell an agent: preferred patterns (e.g. "always use pydantic models for config, not
dataclasses"), things to avoid (e.g. "don't add new dependencies without asking"),
naming conventions for a particular subsystem, or links to ADRs / design docs that
explain *why* the codebase looks the way it does.
-->

## Testing instructions

- Tests live under `tests/`, split into `tests/unit/` (fast, no external
    dependencies) and `tests/integration/` (may exercise CLI entry points, notebooks,
    or other slower paths).
- Run the full suite with `pixi run test`. To iterate quickly on a single test file
    or `-k` expression while debugging, `pixi run pytest <args>` works too, but always
    confirm with the full `pixi run test` before calling something done -- it also
    reports whether combined coverage still clears the threshold set in
    `[tool.coverage.report]`.
- New behavior needs a test. Bug fixes should add a regression test that fails
    without the fix.

<!--
If this project has integration tests that require credentials, network access, a
running service, or other setup an agent might not have, say so here, and say
whether the agent should skip them, mock them, or ask a human to run them.
-->

## Documentation

- Documentation source lives under `docs/` as Markdown, built with
    [Zensical](https://zensical.org/) (configured in `zensical.toml`) and published to
    GitHub Pages.
- API reference docs are generated from docstrings via `mkdocstrings` -- add a new
    `::: module.path` line to `docs/reference.md` for any new module that should appear
    in the API reference; it is not automatic.
- Update `docs/release_notes.md` for user-facing changes, but never write real content
    into the `## X.Y.Z (YYYY-MM-DD)` section at the top of the file -- that's a
    reusable template (see the HTML comment inside it), not a place to record actual
    changes. Add your change to the first real, numbered section below it instead,
    which represents the upcoming/unreleased version; create that section (by copying
    the template) if it doesn't already exist. Use `pymdownx.magiclink` shorthand for
    PR/issue references (`!123` for a pull request, `#123` for an issue) rather than
    full GitHub URLs.
- Don't trust the file's existing top section number alone to know what the next
    version is -- it can lag behind reality (e.g. a release cut and tagged without the
    file being updated to match). Before adding or creating an unreleased section, run
    `git tag --sort=-v:refname | head -1` to find the actual most-recently-released
    version, and base the next number on that instead. This repo bumps the patch
    version (the `Z` in `X.Y.Z`) for ordinary PRs; only bump minor/major if asked to.
    If the version you're about to write already exists as a tag, stop and reconcile
    the mismatch (e.g. by asking) rather than silently overwriting or renumbering.
- Write prose using semantic linefeeds (one sentence, or one independent clause, per
    line) rather than hard-wrapping at a fixed column. This keeps diffs to the
    sentence that actually changed instead of reflowing the whole paragraph.
    `mdformat` won't fight this -- its default `wrap: keep` behavior preserves
    whatever line breaks are already there rather than rejoining and rewrapping
    paragraphs -- but nothing enforces it automatically either, so it's on you (or
    the agent) to actually break lines this way when writing new prose.

<!--
If this project has other documentation conventions -- a changelog format, ADRs, a
glossary of domain terms agents should learn before touching certain code -- list
them here.
-->

## Commit / PR instructions

<!--
Describe the expected commit message format (e.g. Conventional Commits), whether PRs
need a particular template filled out, what CI needs to pass before merge, and who
needs to review changes to sensitive areas of the code.
-->

- Before committing, run `pixi run format`, `pixi run lint`, and `pixi run test`; CI
    (`.github/workflows/pytest.yml`) runs the same checks and will fail the PR
    otherwise.
- \[Add commit message conventions, PR template requirements, and review expectations
    specific to this project.\]

## Security & data handling

<!--
Call out anything an agent should never do without asking: touching production
credentials or infrastructure, modifying published data outputs, changing anything
under a compliance-sensitive directory, adding a new external dependency or service
integration, etc. If there's nothing project-specific beyond normal good judgement,
it's fine to delete this section.
-->

\[Replace or delete: e.g. "Never commit files under `secrets/` or `.env*`." / "This
package processes personal data -- see docs/privacy.md before changing anything in
`src/<package>/pii.py`."\]

## Gotchas

<!--
The stuff that isn't obvious from reading the code: known footguns, parts of the
codebase that are mid-refactor, dependencies that are pinned for a non-obvious
reason, CI flakiness, or "we tried X and it didn't work because Y." This is the
section most worth keeping honest and up to date -- it's where agents save the most
time by not re-discovering a problem someone already solved.
-->

- [Add project-specific gotchas as you discover things worth remembering.]
