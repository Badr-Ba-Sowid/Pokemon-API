import Constants

from Pokemon import Pokemon

from Constants import *


class DataParser:

    def __init__(self, pokemon_data, location_data):
        self.pokemon_data = pokemon_data
        self.location_data = location_data
        self.__encounters = dict()
        self.__name = ''
        self.__pokemon_id = ''

    def get_poke_object(self):
        self.parse_name_id()
        self.parse_location_encounters()

        name = self.__name
        pokemon_id = self.__pokemon_id
        encounter_location = self.__encounters

        pokemon = Pokemon(name, pokemon_id, encounter_location)
        return pokemon

    def parse_location_encounters(self):
        # location_data contains multiple locations
        # each location contains multiple enocunter methods
        try:
            for location in self.location_data:
                location_name = location[LOCATION_AREA][NAME]
                encounter_methods = []
                for encounter_details in location[VERSION_DETAILS]:
                    for encounter_method in encounter_details[ENCOUNTER_DETAILS]:
                        encounter_methods.append(encounter_method[METHOD][NAME])
                self.__encounters[location_name] = encounter_methods
        except KeyError:
            # TODO handle error
            pass

    def parse_name_id(self):
        self.__name = self.pokemon_data[NAME]
        self.__pokemon_id = self.pokemon_data[ID]
