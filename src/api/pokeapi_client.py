import requests


class PokeAPIClient:
    def __init__(self, base_url='https://pokeapi.co/api/v2'):
        """
        Initializes the API client with a base URL.
        :param base_url: The base URL of the PokeAPI.
        """
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'PokeAPIClient/1.0'})

    def get_pokemon(self, id_or_name):
        """
        Fetches details of a Pokémon by its ID or name.
        :param id_or_name: The ID or name of the Pokémon.
        :return: Pokémon details as a dictionary.
        """
        try:
            response = self.session.get(f"{self.base_url}/pokemon/{id_or_name}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            print(f"Error fetching Pokémon with ID/Name '{id_or_name}': {error}")
            raise ValueError(f"Unable to fetch Pokémon data for {id_or_name}")

    def get_generation(self, id_or_name):
        """
        Fetches details of a generation by its ID or name.
        :param id_or_name: The ID or name of the generation.
        :return: Generation details as a dictionary.
        """
        try:
            response = self.session.get(f"{self.base_url}/generation/{id_or_name}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            print(f"Error fetching Generation with ID/Name '{id_or_name}': {error}")
            raise ValueError(f"Unable to fetch Generation data for {id_or_name}")

    def get_paginated_results(self, endpoint, limit=20, offset=0):
        """
        Generic method to fetch paginated results.
        :param endpoint: API endpoint to fetch paginated data.
        :param limit: Number of items per page.
        :param offset: The offset for pagination.
        :return: Paginated results from the API.
        """
        try:
            response = self.session.get(
                f"{self.base_url}/{endpoint}",
                params={'limit': limit, 'offset': offset}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            print(f"Error fetching paginated results from '{endpoint}': {error}")
            raise ValueError(f"Unable to fetch data from {endpoint}")