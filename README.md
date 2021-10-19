# menu.py
<img alt="PyPI" src="https://img.shields.io/pypi/v/menu.py?color=6724ff&label=menu.py&style=flat-square"> <img alt="platform" src="https://img.shields.io/badge/platform-windows-6724ff?style=flat-square"> <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/menu.py?color=6724ff&style=flat-square"> <img alt="PyPI - License" src="https://img.shields.io/pypi/l/menu.py?color=6724ff&style=flat-square"> <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/readyyeti/menu.py?color=6724ff&style=flat-square">

<sup><sub>created by deadyeti (deadyeti@deadyeti.ca)</sub></sup></br>

## Introduction ##

**menu.py** is still in the early stages of development, it is not recommended that you download this package at this time.
</br>

**menu.py** is a lightweight and easy-to-use python module used to quickly and efficiently create in-terminal menus that work in both *Command Prompt* and *Windows PowerShell*. Using **menu.py**, a developer can either create a selection menu, where users select an option from a pre-determined list of options, ~~or a user-input menu, where users type their input.~~ (in development)
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
```
$ git clone https://github.com/readyyeti/menu.py
$ cd menu
$ python 3 -m pip install
```
</br>


## Quick Example ##

```python
from menu import *
from time import sleep

example_menu = menu('app_or_file_name')
theme = 'purple'

def main_menu():

   # setting up the page name and menu options
   page_name = 'main menu'
   text = [
      'please choose from the following options:'
   ]
   options = [
      'option #1',    # CASE 1
      'option #2',    # CASE 2
      '_skip_',       # _skip_ is ignored by menu.py
      'exit'          # CASE 3
   ]

   # generate menu
   selection = example_menu.generate_selection(page_name, options, text, theme)

   match selection:
      case 1:
         print('option 1'), sleep(2)
      case 2:
         print('option 2'), sleep(2)
      case 3:
         example_menu.terminate()
         exit()
   
   return

while True:
   main_menu()

```
</br>

For a more in-depth example, check out the *example.py* file
