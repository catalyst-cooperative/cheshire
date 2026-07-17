FROM ghcr.io/prefix-dev/pixi:0.72.2

# Create a non-root user inside the container
RUN useradd -Ums /bin/bash catalyst

# Copy the cloned repository into the user's home directory
COPY --chown=catalyst:catalyst . /home/catalyst/cheshire

# Switch to being the catalyst user and go into the copied repo
USER catalyst
WORKDIR /home/catalyst/cheshire

# Create the pixi environment based on the specification in pyproject.toml.
# We need information from .git to get version with setuptools_scm so we mount that
# directory without copying it into the image.
RUN --mount=type=bind,source=.git,target=/home/catalyst/cheshire/.git \
    pixi install

# Run the tests to verify that everything is functioning:
CMD ["pixi", "run", "test"]
