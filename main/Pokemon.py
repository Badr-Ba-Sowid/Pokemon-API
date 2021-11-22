class Pokemon:

    def __init__(self, name, poke_id, encounter_location):
        self.__name = name
        self.__id = poke_id
        self.__encounterLocation = encounter_location

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_encounter_location(self):
        return self.__encounterLocation

    def display_pokemon(self):
        print("\033[1m  Pokemon ID  \033[0m", self.get_id() , "\n")
        print("\033[1m  Pokemon Name  \033[0m", self.get_name() , "\n")
        for key, value in self.__encounterLocation.items():
            print("\033[1m  Location Name  \033[0m", key)
            print("\033[1m  Encounter method(s)  \033[0m", set(value), "\n")

