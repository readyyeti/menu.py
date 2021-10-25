from os import DirEntry
from time import sleep
import random 

if __package__:
    from .exceptions import *
else: # testing purposes
    from sys import path
    from os import path as directory
    path.append(directory.dirname(__file__) + '\\exception.py')
    from exceptions import *

from configparser import ConfigParser

__all__ = [
    'colors',

]

supported_themes = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'default'
]
themes_list = '\n - '+'\n - '.join(supported_themes)+'\n '

# foreground color codes
class foreground:

    black       = '\033[30m'
    red         = '\033[31m'
    green       = '\033[32m'
    yellow      = '\033[33m'
    blue        = '\033[34m'
    magenta     = '\033[35m'
    cyan        = '\033[36m'
    white       = '\033[37m'
    default     = '\033[39m'

# background color codes
class background:

    black       = '\033[40m'
    red         = '\033[41m'
    green       = '\033[42m'
    yellow      = '\033[43m'
    blue        = '\033[44m'
    magenta     = '\033[45m'
    cyan        = '\033[46m'
    white       = '\033[47m'
    default     = '\033[49m'

class color:

    # header colors    fore / back
    title            = foreground.white
    page             = foreground.white
    header           = foreground.white

    # menu_text colors
    menu_text        = foreground.white

    # input colors
    prompt           = foreground.white
    user_input       = foreground.white

    # menu option colors
    idle_opt         = foreground.white
    active_opt       = foreground.white

    # end
    _end              = foreground.default+background.default

class theme(object):

    def __init__(self, theme:str = 'white'):
        if type(theme) != str:
            raise menu_type_exception(f'class parameter "theme" must be a string, not {type(theme)}')

        # applk theme
        if theme.lower() in ['custom', 'complex']:
            self.theme = None
        elif theme not in supported_themes:
            if len(theme) <= 16:
                raise menu_exception(f'\n"{theme}" is not a theme supported by menu.py\nplease select one of the following themes:\n{themes_list}')
            else:
                raise menu_exception(f'\nthe theme you selected is not a theme supported by menu.py\nplease select one of the following themes:\n{themes_list}')
        else:
            self.theme = theme
            if theme != None:
                set_theme(theme)

def set_theme(theme):

    if theme == 'default':
        color.title         = foreground.black+getattr(background, 'white')
        color.active_opt    = foreground.black+getattr(background, 'white')
    else:
        color.title         = foreground.black+getattr(background, theme)
        color.active_opt    = foreground.black+getattr(background, theme)
    color.page         = getattr(foreground, theme)
    color.header        = getattr(foreground, theme)
    color.menu_text     = getattr(foreground, theme)
    color.idle_opt      = getattr(foreground, theme)
    color.prompt        = getattr(foreground, theme)
    color.user_input    = getattr(foreground, theme)

last_theme = ''
while True:
        a2 = random.choice(supported_themes)
        while a2 == last_theme:
            a2 = random.choice(supported_themes)
        theme(a2)
        last_theme = a2

        print('')
        print(f'{color.title} title {color._end}')
        print(f'{color.page} page {color._end}')
        print(f'{color.header} header {color._end}')
        print(f'{color.menu_text} menu_text {color._end}')
        print(f'{color.idle_opt} idle_opt {color._end}')
        print(f'{color.active_opt} active_opt {color._end}')
        print(f'{color.prompt} prompt {color._end}')
        print(f'{color.user_input} page {color._end}')
        print('')
        input(' press any key to restart l00p...')
