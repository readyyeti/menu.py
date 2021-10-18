choice = 1
last_page = ''
last_teme = ''
last_theme = ''

import keyboard as k
from time import sleep
from menu_functions import *
from theme import *

__all__=[
    'menu',
    'menuException',
]

# exception masterclass
class menuException(Exception):
    def __init__ (self, message):
        self.message = message

# menu master class
class menu(object):

    def __init__(self, program_name):
        self.name = program_name

    def generate_input(self, page_name, menu_text:list = None, input_msg:str = None, theme:str = None):

        '''
        generates an in-terminal user-input menu that works both in windows command-prompt and powershell.

        '''

        global last_theme
        # only set the theme when applicable
        if last_theme != theme:
            if theme != None:
                color_theme.set_theme(theme)              
        last_theme = theme

        cls()
        print_header(self.name, page_name)

        if menu_text != None:
            if isinstance(menu_text, str) == True:
                print(f' {color_theme.text}{menu_text}{color_theme.end}')
            elif isinstance(menu_text, list) == True:
                for item in menu_text:
                    if item == '_skip_':
                        print('')
                        continue
                    print(f' {color_theme.text}{item}{color_theme.end}')
            else:
                menuException('menu_text must be either a string or a list')
            print('')
        
        if input_msg != None:
            input(f' {input_msg}: ')
        else:
            input(' ')

        return str(input)


    def generate_selection(self, page_name, menu_items:list, menu_text:list = None, theme:str = None):

        '''
        generates an in-terminal user-selection menu that works both in windows command-prompt and powershell.

        '''

        # self setup
        #theme = theme
        #program_name = program_name
        #page_name = page_name
        #menu_items = menu_items
        #if menu_text != None:
        #    menu_text = menu_text

        global choice     
        global last_page
        global last_theme

        # this ensures that when changing pages, the selection returns to the top of the page
        if last_page != '':
            if last_page != page_name:
                choice = 1
        else:
            choice = 1
        last_page = page_name

        # only set the theme when applicable
        if last_theme != theme:
            if theme != None:
                color_theme.set_theme(theme)
                
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

        cls()                                    #clears the terminal screen
        print_header(self.name, page_name)       #prints the menu header

        # prints optional menu_text, if there is any.
        if menu_text != None:
            if isinstance(menu_text, str) == True:
                print(f' {color_theme.text}{menu_text}{color_theme.end}')
            elif isinstance(menu_text, list) == True:
                for item in menu_text:
                    if item == '_skip_':
                        print('')
                        continue
                    print(f' {color_theme.text}{item}{color_theme.end}')
            else:
                menuException('menu_text must either be a string or a list')
            print('')

        # if no menu options are present, raise exception (can't have a menu with no options, can you?).
        if len(menu_items) <= 0:
            raise Exception('menu must contain at least one menu item')

        # print menu items
        i = 1
        if isinstance(menu_items, str) == True:
            menu_option(i, item, True).print()
        elif isinstance(menu_items, list) == True:
            for item in menu_items:
                if item == '_skip_':
                    print('')
                    continue
                if i == choice:
                    menu_option(i, item, True).print()
                else:
                    menu_option(i, item).print()
                i += 1
        else:
            menuException('menu_items must either be a string or a list')

        # l00p until user selects an item in the menu
        sleep(0.22)
        while not k.is_pressed('up arrow'):
            if k.is_pressed('right arrow'):
                choice += 1
                self.generate_selection(page_name, menu_items, menu_text, theme)
            elif k.is_pressed('left arrow'):
                choice -= 1
                self.generate_selection(page_name, menu_items, menu_text, theme)
            sleep(0.01)
        
        return menu_option(choice, menu_items[choice-1], menu_items[choice-1]).select()

    def terminate(self):
        print(f'menu "{self.name}", page "{self.page}" has been deleted..'), sleep(2)
        del self

# menu_option subclass
class menu_option(menu):

    def __init__(self, number:int, name:str, bHighlight:bool = False):
        self.number = number
        self.name = name
        self.bHighlight = bHighlight

    def print(self):
        if self.bHighlight == False:
            print(f' {color_theme.text} {self.name} {color_theme.end}')
        else:
            print(f' {color_theme.highlight} {self.name} {color_theme.end}')
        return

    def select(self):
        return self.number

        

