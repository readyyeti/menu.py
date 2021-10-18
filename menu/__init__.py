"""
menu.py
=============================================
a simple python library for creating in-terminal menus.

copyright (c) 2021-present deadyeti

MIT License, see LICENSE for more details.
"""

# import functions
#from .menu import generate
#from .menu import terminate

# import classes
#from .menu import cprint
#from .menu import eprint

# import variables
from .menu import *
from classes.menu_classes import *

__all__ = [
    'generate',
    'cprint',
    'eprint',
    'terminate',
    '__title__',
    '__author__',
    '__license__',
    '__copyright__',
    '__version__'
]

__title__ = 'menu'
__author__ = 'deadyeti'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present deadyeti'
__version__ = version