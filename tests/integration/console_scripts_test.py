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


@pytest.mark.parametrize("alpha,beta", [("2", "2")])
@pytest.mark.script_launch_mode("inprocess")
def test_winston_valid_args(script_runner, alpha: str, beta: str) -> None:
    """Running the script with valid integer arguments should succeed."""
    ret = script_runner.run(["winston", "--alpha", alpha, "--beta", beta])
    assert ret.success  # nosec: B101


@pytest.mark.parametrize(
    "alpha,beta",
    [
        ("a", "2"),
        ("2", "b"),
        ("a", "b"),
    ],
)
@pytest.mark.script_launch_mode("inprocess")
def test_winston_invalid_args(script_runner, alpha: str, beta: str) -> None:
    """Non-integer arguments should be rejected by argparse, not silently accepted."""
    ret = script_runner.run(["winston", "--alpha", alpha, "--beta", beta])
    assert not ret.success  # nosec: B101
    assert ret.returncode == 2  # nosec: B101
    assert "invalid int value" in ret.stderr
