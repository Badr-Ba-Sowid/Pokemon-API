from Constants import POKEMON_BASE_URL, POKEMON_DETAILS_URL


class QueryBuilder:
    def __init__(self, query):
        self.query = query

    def get_pokemon_details(self):
        return POKEMON_DETAILS_URL + self.query + "/"

    def get_pokemon_locations(self):
        return POKEMON_BASE_URL + self.query
