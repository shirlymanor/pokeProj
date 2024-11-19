import unittest
import os
import sys
sys.path.append(os.path.dirname(__file__) + '/..')

from api.pokeapi_client import PokeAPIClient

class TestPokeAPIClient(unittest.TestCase):
    def setUp(self):
        self.client = PokeAPIClient()

    def test_get_pokemon(self):
        pokemon = self.client.get_pokemon('pikachu')
        print(pokemon)
        
    def test_get_generation(self):
        try:
            generation = self.client.get_generation(1000)
            print(generation)
        except Exception as e:
            print(e)
    

if __name__ == '__main__':
    unittest.main()