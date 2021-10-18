
from time import sleep

__all__=[
    'color_theme'
]

class color_theme:

    # default color theme (white)
    text = '\33[37m'
    highlight = '\33[7m'
    error = '\033[91m'
    title = '\33[7m'
    page = '\33[37m'
    end = '\033[0m'

    def set_theme(color:str):
        if color.lower() in ['blue', 'bleu']:
            color_theme.text = '\33[34m'
            color_theme.highlight = '\33[44m\033[30m'
            color_theme.error = '\033[91m'
            color_theme.title = '\33[44m\033[30m'
            color_theme.page = '\33[34m'
        else: #sets the default theme
            pass

        return