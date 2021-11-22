from ApiClient import ApiClient
from Constants import INVALID_QUERY,ERROR_MESSAGE
from DataParser import DataParser


def get_pokemon(query):
    # intialize api client and get data in raw json

    apiClient = ApiClient()
    name_id_data, location_encounter_data = apiClient.query_pokemon(query)
    if isinstance(name_id_data, int):
        print(ERROR_MESSAGE, name_id_data)
        return None
    elif isinstance(location_encounter_data , int):
        print("We enconutered an error , status code:", location_encounter_data)
        return None
    else:
        # use dataparser class to get a custom Pokemon object
        dataParser = DataParser(name_id_data, location_encounter_data)
        return dataParser.get_poke_object()


def valid_query(query):
    return query.isspace() or query == ""



def main():
    while True:
        user_input = input("Enter the name or id of the pokemon or enter Q to exit")
        if user_input == "Q" or user_input == "q":
            break
        else:
            if valid_query(user_input):
                print(INVALID_QUERY)
            else:
                pokemon = get_pokemon(user_input)
                if pokemon is not None:
                    pokemon.display_pokemon()


if __name__ == "__main__":
    main()


