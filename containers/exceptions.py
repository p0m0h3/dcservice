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
