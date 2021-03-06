"""Decorators stuff"""
import os
import sys

from flaskbox import constants


def if_file_exists(func):
    """Check if file exists"""
    def file_exists(*args, **kwargs):
        """
        If flaskbox.yml file exists
        Print message and exit from the program.
        """
        if os.path.isfile('flaskbox.yml'):
            print(constants.FILE_EXISTS_MESSAGE)
            sys.exit(1)
        return func(*args, **kwargs)
    return file_exists


def file_not_exists(func):
    """File not exists"""
    def not_exists(*args, **kwargs):
        """If file not exists, return the message"""
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(constants.NOT_EXISTS_MESSAGE)
            sys.exit(1)
    return not_exists
