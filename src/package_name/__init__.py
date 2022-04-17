"""A template repository for a Python package created by Catalyst Cooperative."""
import logging

import pkg_resources

__author__ = "Catalyst Cooperative"
__contact__ = "pudl@catalyst.coop"
__maintainer__ = "Individual Cat"
__license__ = "MIT License"
__maintainer_email__ = "individual.cat@catalyst.coop"
__version__ = pkg_resources.get_distribution("package_name").version
__docformat__ = "restructuredtext en"
__description__ = "A template for Python package repositories."
__long_description__ = """
This should be a paragraph long description of what the package does.
"""
__projecturl__ = "https://github.com/catalyst-cooperative/package_name/"
__downloadurl__ = "https://github.com/catalyst-cooperative/package_name/"

# Create a root logger for use anywhere within the package.
logging.getLogger(__name__).addHandler(logging.NullHandler())
