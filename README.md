# menu.py
[![PyPI](https://img.shields.io/pypi/v/menu.py?color=6724ff&label=PyPI&style=flat-square)](https://pypi.org/project/menu.py/)
[![Platform](https://img.shields.io/badge/platform-windows-6724ff?style=flat-square)](https://pypi.org/project/menu.py/)
[![Version](https://img.shields.io/badge/python-3.6%2B-6724ff)](https://pypi.org/project/menu.py/)
[![GitHub last commit](https://img.shields.io/github/last-commit/readyyeti/menu.py?color=6724ff&style=flat-square)](https://github.com/readyyeti/menu.py)
<br>
<br>

> ### created by: deadyeti
> - [Contact via e-mail](mailto:deadyeti@deadyeti.ca)
> - [Contact via discord](https://discordapp.com/users/323651600990339074)
>
<br>

> ### links
> - [view on github](https://www.github.com/readyyeti/menu.py)
> - [view on PyPI](https://pypi.org/project/menu.py/)
>
<br>
<br>

## Introduction ##


> ## ⚠️ 
>
> - **menu.py** is still in the early stages of development, it is not recommended that you download this package at this time.
> - **menu.py** only works on machines running Windows.
>
<br>

**menu.py** is a lightweight and easy-to-use python package used to quickly and efficiently create in-terminal menus that work in both *Command Prompt* and *Windows PowerShell*. Using **menu.py**, a user can either create a selection menu, where one selects an option from a pre-determined list of options, ~~or a user-input menu, where users type their input.~~ (not yet implemented)
</br>


## Key Features ##

   ✔️ fast and efficient<br/>
   ✔️ supports the use of colors<br/>
   ✔️ variable refresh-rate<br/>
   ✔️ easy to use<br/>
   ✔️ actively supported<br/>
</br>


## Installation ##

To install this module using pip:
```
py -m pip install menu.py
```

</br>

I always try to keep the most up-to-date version on pypi, but in case you need to install the most up-to-date version from github:
```git
$ git clone https://github.com/readyyeti/menu.py
$ cd menu.py
$ py -m pip install -U
```
</br>


## Quick Example ##

```python
from menu import *
from time import sleep

example_menu = menu('app_or_file_name')
theme = 'blue'

def main_menu():

   # setting up the page name and menu options
   page_name = 'name_of_page'
   text = [
      'please choose from the following options:'
   ]
   options = [
      'option #1',    # CASE 1
      'option #2',    # CASE 2
      '_skip_',       # # "_skip_", " " and "" can be used to create a blank line without messing up the selections
      'exit'          # CASE 3
   ]

   # generate menu
   selection = example_menu.generate(page_name, options, text, theme)

   match selection:
      case 1:
         menuprint('you selected option 1'), sleep(2)
      case 2:
         menuprint('you selected option 2'), sleep(2)
      case 3:
         example_menu.terminate()
         return exit()
   
   return

while True:
   main_menu()

```
</br>

For a more in-depth example, check out the *example.py* file
