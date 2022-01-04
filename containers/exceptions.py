"""
Module Exceptions
"""


class ArgumentNotFound(Exception):
    """
    raised when a requested argument is not sent to start a task with.
    """


class ToolNotFound(Exception):
    """
    raised when a requested tool is not defined to start a task with.
    """


class ContainerNotExited(Exception):
    """
    raised when a container log is not yet complete to be fetched
    """


class ContainerNotFound(Exception):
    """
    raised when a refered container is not found
    """
