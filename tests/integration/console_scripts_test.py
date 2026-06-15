"""Test the PUDL console scripts from within PyTest."""

import importlib.metadata

import pytest

# Obtain a list of all deployed entry point scripts to test:
ENTRY_POINTS = importlib.metadata.distribution("catalystcoop.cheshire").entry_points


@pytest.mark.parametrize("ep", ENTRY_POINTS)
@pytest.mark.script_launch_mode("inprocess")
def test_pudl_scripts(script_runner, ep: importlib.metadata.EntryPoint) -> None:
    """Run each deployed console script with --help as a basic test.

    The script_runner fixture is provided by the pytest-console-scripts plugin.
    """
    ret = script_runner.run([ep.name, "--help"], print_result=False)
    assert ret.success  # nosec: B101


@pytest.mark.parametrize(
    "alpha,beta",
    [
        ("2", "2"),
        pytest.param("a", "2", marks=pytest.mark.xfail),
        pytest.param("2", "b", marks=pytest.mark.xfail),
        pytest.param("a", "b", marks=pytest.mark.xfail),
    ],
)
@pytest.mark.script_launch_mode("inprocess")
def test_winston_args(script_runner, alpha: str, beta: str) -> None:
    """Try running the script with bad inputs."""
    ret = script_runner.run(["winston", "--alpha", alpha, "--beta", beta])
    assert ret.success  # nosec: B101
