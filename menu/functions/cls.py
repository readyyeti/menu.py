from os import system, name

__all__=[
    'cls'
]

# function that clears the terminal screen when called
def cls():
    system('cls' if name=='nt' else 'clear')
    return