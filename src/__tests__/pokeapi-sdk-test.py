import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.pokeapi_client import PokeAPIClient

# Test the get_pokemon method
client = PokeAPIClient()
try:
    pokemon = client.get_pokemon('pikachu')
    print(pokemon)
except ValueError as e:
    print(f"An error occurred: {e}")
# Test the get_generation method
try:
    generation = client.get_generation(1)
    print(generation)
except ValueError as e:
    print(f"An error occurred: {e}")