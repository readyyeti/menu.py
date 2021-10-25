from time import sleep

class menuconfig(object):

    def __init__(self):
        self.theme = ''
        


class alpha(menuconfig):
    def __init__(self, name:str):
        self.name = name
        self.age = ''
        if self.age != '':
            print(f' name: {self.name}\n age: {self.age}'), sleep(2)
        else:
            print(f' name: {self.name}')

    def set_age(self, age:int):
        str(age) = self.age

alpha('nicole')
input(' >> END: press enter to continue..')