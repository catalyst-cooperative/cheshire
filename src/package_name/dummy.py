"""A dummy module so coverage has something to cover."""
import logging

logger = logging.getLogger(__name__)


def do_something(a: int, b: int):
    """A dummy function that does something."""
    logger.debug("Don't just do something, stand there!")
    c = a + b
    return c
