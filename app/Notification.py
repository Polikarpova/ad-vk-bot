class Notification:
    def __init__(self, name, date):
        self.__name = name
        self.__date = date

    @property
    def name(self):
        return self.__name

    @name.setter
    def message(self, message):
        self.__message = message

    @property
    def date(self):
        return self.__date

    # Принимает timestamp
    @date.setter
    def date(self, timestamp):
        self.__date = timestamp
