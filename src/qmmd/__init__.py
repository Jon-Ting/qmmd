"""
QMMD Package
==================

Documentation is available in two forms: docstrings provided with the code, 
and a loose standing reference guide, available from 
`the QMMD homepage <https://qmmd.readthedocs.io/en/latest/>`_.
"""
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version('qmmd')
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ['mdsim', 'qmcalc', 'datasets', 'test']

from qmmd import mdsim
from qmmd import qmcalc
from qmmd import datasets


def test():
    """Run tests for the qmmd package."""
    import pytest
    import os
    package_path = os.path.dirname(__file__)
    test_path = os.path.join(os.path.dirname(package_path), 'tests')
    if not os.path.exists(test_path):
        # If installed as a package, tests might be inside the package or elsewhere
        # For now, assume it's run from the source tree or tests are installed
        print(f"Could not find tests directory at {test_path}")
        return
    pytest.main([test_path])
