command_list = []

class Command:
    def __init__(self):
        self.__keys = []
        self.desription = ''
        command_list.append(self)

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, mass):
        for key in mass:
            self.__keys.append(key.lower())

    def proccess(self, data):
        pass
