FROM ghcr.io/prefix-dev/pixi:0.72.2

# Create a non-root user inside the container
RUN useradd -Ums /bin/bash catalyst

# Copy the cloned repository into the user's home directory
COPY --chown=catalyst:catalyst . /home/catalyst/cheshire

# Switch to being the catalyst user and go into the copied repo
USER catalyst
WORKDIR /home/catalyst/cheshire

# hatch-vcs normally derives the package version from `.git`, but can't do that
# reliably from inside a Docker build. Instead, accept the version as a build
# argument -- computed from git history by the caller (see
# .github/workflows/docker-build-push.yml).
ARG PACKAGE_VERSION

# hatch-vcs gets its version by calling the setuptools-scm *library* under the hood
# (even though we don't use setuptools-scm as our build backend), and that library
# looks for this exact, non-configurable environment variable name as a fallback
# when it can't read git metadata directly -- do not rename it. It must also be the
# plain SETUPTOOLS_SCM_PRETEND_VERSION, not a dist-name-specific "_FOR_<NAME>"
# variant: hatch-vcs's call into setuptools-scm never passes a dist_name, so
# setuptools-scm has no way to know which dist-specific suffix to look for.
ENV SETUPTOOLS_SCM_PRETEND_VERSION=$PACKAGE_VERSION

# Create the pixi environment based on the specification in pyproject.toml.
RUN pixi install

# Run the tests to verify that everything is functioning:
CMD ["pixi", "run", "test"]
