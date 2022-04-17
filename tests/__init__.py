"""Test modules for discovery by pytest."""
# Create a parent logger for all test loggers to inherit from
import logging

logging.getLogger(__name__).addHandler(logging.NullHandler())
