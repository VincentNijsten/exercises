class Wizard:
    def __init__(self, name):
        self.__mane = 45
        self.__health = 65 
        self.name = name       

    def get_mana(self):
        return self.__mane

    def get_health(self):
        return self.__health
