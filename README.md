# yetimenu.py
<sup><sub>created by deadyeti (deadyeti@deadyeti.ca)</sub></sup>

## introduction ##

**yetimenu.py** is a lightweight and easy-to-use python module used to quickly and efficiently create in-terminal menus that work in both *Command Prompt* and *Windows PowerShell*. Using **yetimenu.py**, a developer can either create a selection menu, where users select an option from a pre-determined list of options, or a user-input menu, where users type their input.

<sup><sub>**Note**:**yetimenu** *only displays a menu and returns the user selection/input, it does not handle user selection/input*. For a more in-depth look at how yetimenu works, please look at yetimenu/example.py</sub></sup>
</br>

## key features ##

   ✔️ fast and efficient<br/>
   ✔️ supports the use of colors<br/>
   ✔️ variable refresh-rate<br/>
   ✔️ easy to use<br/>
   ✔️ actively supported<br/>
</br>

## Installation ##

#### ⚠️ This module only works on Windows
#### ⚠️ python 3.6 or greater **required** <sup><sub>python 3.10 or greater recommended</sub></sup>
</br>

To install this module using pip:
```
py -m pip install yetimenu.py
```

</br>

I always try to keep the most up-to-date version on pypi, but in case you need to install the most up-to-date version from github:
```
$ git clone https://github.com/readyyeti/yetimenu.py
$ cd yetimenu
$ python 3 -m pip install
```
</br>

## Quick Example ##

```python
import yetimenu.py as menu

app_name = 'example'
theme = 'purple'

def main_menu()

   page_name = 'main menu'
   text = [
      'please choose from the following options:'
   ]
   options = [
      'option #1',    # CASE 1
      'option #2',    # CASE 2
      '_skip_',       # _skip_ is ignored by yetimenu
      'exit'          # CASE 3
   ]

   menu_type = 'selection'
   selection = m.generate(menu_type, theme, app_name, page_name, options, text)

   match selection:
      case 1:
         print('option 1')
      case 2:
         print('option 2')
      case 3:
         m.terminate()
   
   return

main_menu()

```
</br>

For a more in-depth example, check out the *examples.py* file
