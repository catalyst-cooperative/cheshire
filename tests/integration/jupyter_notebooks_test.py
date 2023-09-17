"""Test any Jupyter notebooks in the repo that we're maintaining."""
from pathlib import Path

import nbformat
import pytest
from nbconvert.preprocessors.execute import ExecutePreprocessor


@pytest.mark.parametrize(
    "notebook",
    [
        "notebooks/notebook.ipynb",
    ],
)
def test_notebook_exec(notebook: str, test_dir: Path):
    """Test that maintained notebooks can be executed."""
    nb_path = test_dir.parent / notebook
    with nb_path.open() as f:
        nb = nbformat.read(f, as_version=4)
        ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
        _ = ep.preprocess(nb, resources={"Application": {"log_level": 5}})
