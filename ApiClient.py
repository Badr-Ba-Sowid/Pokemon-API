import requests
from Constants import INVALID_QUERY
import requests_cache
from QueryBuilder import QueryBuilder
from Constants import LOCATION_AREA_ENCOUNTERS


class ApiClient:

    def __init__(self):
        requests_cache.install_cache(expire_after=86400, backend="sqlite")

    def get_name_id(self, query):
        trimmed_query = query.strip()
        url = QueryBuilder(trimmed_query).get_pokemon_details()
        response = requests.get(url, params="query")
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_location(self, link):
        if link is not None:
            response = requests.get(link, params="query")
            if response.status_code == 200:
                return response.json()
            else:
                return response.status_code

    def query_pokemon(self, query):
        location_area_encounters = ""
        name_id_json = self.get_name_id(query)
        # check if the first request is of type int
        # meaning that it returns a status code instead of json
        if isinstance(name_id_json, int):
            return name_id_json, None
        try:
            location_area_encounters = name_id_json[LOCATION_AREA_ENCOUNTERS]
        except KeyError:
            # return 404 as the resource location_area_encounters doesn't exist
            return None, 404
        location_encounter_data = self.get_location(location_area_encounters)

        return name_id_json, location_encounter_data
