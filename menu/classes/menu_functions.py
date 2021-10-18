from os import system, name
from theme import *

__all__=[
    'cls',
    'print_header'
]

# function that clears the terminal screen when called
def cls():
    system('cls' if name=='nt' else 'clear')
    return

# function that prints the terminal header when called
def print_header(program_name, page_name):
    if page_name != None:
        print(f' {color_theme.title} {program_name} {color_theme.end} {color_theme.text}::{color_theme.end}{color_theme.page} [ {page_name} ]{color_theme.end}\n')
    else:
        print(f' {color_theme.title}  {program_name}  {color_theme.end}\n')
