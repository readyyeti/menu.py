import os
from time import sleep
import random as r
from configparser import ConfigParser
from types import FunctionType
import keyboard as k
from platform import python_version, system, python_version_tuple

bDebug:bool = False

version = '0.1.7'
__all__= (
    'version',
    'generate',
    'terminate',
    'cprint',
    'eprint'
)

last_page = ''
last_theme = ''
choice = 1

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CLASSES 

# this class is used to quickly create different text color in the python terminal

class yetimenuException(Exception):
    def __init__ (self, message):
        self.message = message

class debugPrint:
    def __init__(self, message):

        global bDebug
        self.message = message
    
        if bDebug == True:
            print(f'debug: {self.message}'), sleep(1)

class c:

    title = ''
    text = ''
    highlight = ''
    error = ''
    page = ''
    end = '\033[0m'

class menu_option(object):
    
    def __init__(self, number:int, name:str, bHighlight:bool = False):
        self.number = number
        self.name = name
        self.bHighlight = bHighlight

    def print(self):
        if self.bHighlight == False:
            print(f' {c.text} {self.name} {c.end}')
        else:
            print(f' {c.highlight} {self.name} {c.end}')
        return

    def select(self):
        return self.number

class cprint(object):

    def __init__(self, msg:str, newline=True):
        self.msg = msg
        if newline == True:
            print(f'\n {c.text}{self.msg}{c.end}')
        else:
            print(f' {c.text}{self.msg}{c.end}')

class eprint(object):

    def __init__(self, msg:str, newline:bool=True):
        self.msg = msg
        if newline == True:
            print(f'\n {c.error}*{self.msg}{c.end}')
        else:
            print(f' {c.error}*{self.msg}{c.end}')


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< FUNCTIONS 

#check that user is using the correct OS and version of python
if system().lower() != 'windows':
    raise yetimenuException(f'invalid operating system: "{system()}"\nyetimenu currently only works on windows machines.')
if int(python_version_tuple()[0]) < 3 or int(python_version_tuple()[1]) < 6:
    raise yetimenuException(f'invalid python version: "{python_version()}"\nyetimenu makes use of features, such as f-strings, that require python 3.6 or newer.')

# function that clears the python terminal screen when called
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return

def set_theme(theme):

    # blue theme
    if theme.lower() in ['blue', 'bleu']:
        c.text = '\33[34m'
        c.highlight = '\33[44m\033[30m'
        c.error = '\033[91m'
        c.title = '\33[44m\033[30m'
        c.page = '\33[34m'
    # light blue theme
    elif theme.lower() in ['light blue', 'bleu pâle', 'bleu pale']:
        c.text = '\033[36m'
        c.highlight = '\033[46m\033[30m'
        c.error = '\033[91m'
        c.title = '\033[46m\033[30m'
        c.page = '\033[36m'
    # red theme
    elif theme.lower() in ['red', 'rouge']:
        c.text = '\033[31m'
        c.highlight = '\033[41m\033[30m'
        c.error = '\33[33m'
        c.title = '\033[41m\033[30m'
        c.page = '\033[31m'
    # green theme
    elif theme.lower() in ['green', 'vert']:
        c.text = '\033[32m'
        c.highlight = '\033[42m\033[30m'
        c.error = '\033[91m'
        c.title = '\033[102m\033[30m'
        c.page = '\33[92m'
    # purple theme
    elif theme.lower() in ['purple', 'violet', 'mauve']:
        c.text = '\33[95m'
        c.highlight = '\33[45m\033[30m'
        c.error = '\033[91m'
        c.title = '\33[45m\033[30m'
        c.page = '\33[95m'
    # yellow theme
    elif theme.lower() in ['yellow', 'jaune']:
        c.text = '\33[33m'
        c.highlight = '\33[43m\033[30m'
        c.error = '\033[91m'
        c.title = '\33[43m\033[30m'
        c.page = c.text = '\33[33m'
    # red/purple theme
    elif theme.lower() in ['red/purple', 'rouge/mauve', 'rouge/violet', 'red/violet']:
        c.text = '\033[31m'
        c.highlight = '\033[41m\033[30m'
        c.error = '\33[33m'
        c.title = '\33[45m\033[30m'
        c.page = '\33[35m\033[1m'

    else: #sets the default theme
        c.text = '\33[37m'
        c.highlight = '\33[7m'
        c.error = '\033[91m'
        c.title = '\33[7m'
        c.page = '\33[37m'

    return

# function that prints the terminal header when called
def print_header(program_name, page_name):
    if page_name != None:
        print(f' {c.title} {program_name} {c.end} {c.text}::{c.end}{c.page} [ {page_name} ]{c.end}\n')
    else:
        print(f' {c.title}  {program_name}  {c.end}\n')

# user input function
def user_select(valid_choices): # ....DEPRECATED....

    #choice = None

    choice = input(f' input: ')
    if len(choice) <= 0:
        generate()
    elif choice not in valid_choices:
        generate()
    else:
        selection = int(choice)
        return selection

def terminate():
    cls()
    exit()

# main menu function
def generate(type:str, theme, program_name, page_name, menu_items:list, menu_text:list = None):

    '''
    generates an in-terminal menu that works both in windows command-prompt and powershell.
    
    author: deadyeti

    '''
    global choice 

    # generate the desired menu
    if type.lower() in ['input', 'i']:
        if menu_text == None:
            #_generateInput(theme, program_name, page_name, menu_items)
            pass
        else:
            #_generateInput(theme, program_name, page_name, menu_items)
            pass
    elif type.lower() in ['sel', 'select', 'selection', 's']:
        pass
    else:
        raise yetimenuException(f'invalid menu type: "{type}"\nvalid choices are: selection, input (these can also be written as s or i, respectively)')
    
    global last_page
    global last_theme

    # this ensures that when changing pages, the selection returns to the top of the page
    if last_page != '':
        if last_page != page_name:
            choice = 1
            debugPrint('resetting choice')
    else:
        choice = 1
    last_page = page_name

    # only set the theme when applicable
    if last_theme != theme:
            set_theme(theme) #sets the color theme of the menu
            debugPrint(f'changing theme from {last_theme} to {theme}')
    last_theme = theme

    # get the total amount of menu_options loaded into the menu, minus any "_skip_" options.
    # if the choice goes above or below the number of loaded menu items, return to 1 or total.
    # this ensures that the options scroll in the desired way.
    total_options = 0
    total_options = len(menu_items) - menu_items.count('_skip_')
    if choice > total_options:
        choice = 1
    if choice < 1:
        choice = total_options

    cls()                                       #clears the terminal screen
    print_header(program_name, page_name)       #prints the menu header

    # prints optional menu_text, if there is any.
    if menu_text != None:
        for item in menu_text:
            if item == '_skip_':
                print('')
                continue
            print(f' {c.text}{item}{c.end}')
        print('')

    # if no menu options are present, raise exception (can't have a menu with no options, can you?).
    if len(menu_items) <= 0:
        raise Exception('menu must contain at least one menu item')

    # print menu items
    i = 1
    for item in menu_items:
        if item == '_skip_':
            print('')
            continue
        if i == choice:
            menu_option(i, item, True).print()
        else:
            menu_option(i, item).print()
        i += 1

    # l00p until user selects an item in the menu
    sleep(0.22)
    while not k.is_pressed('up arrow'):
        if k.is_pressed('right arrow'):
            choice += 1
            generate(type, theme, program_name, page_name, menu_items, menu_text)
        elif k.is_pressed('left arrow'):
            choice -= 1
            generate(type, theme, program_name, page_name, menu_items, menu_text)
        sleep(0.01)
    
    return menu_option(choice, menu_items[choice-1], menu_items[choice-1]).select()
        
    # user input field
    selection = user_select(valid_choices)

    # get function from user input data
    menu_option(selection, menu_options[selection-1][0], menu_options[selection-1][1]).__call__()
    sleep(1)
    return