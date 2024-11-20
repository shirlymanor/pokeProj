import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.append(os.path.dirname(__file__))

from sdk.pokeapi_client import PokeAPIClient

def main():
    st.title("Pokémon Information App")

    # Create an instance of PokeAPIClient
    client = PokeAPIClient()

    # Input for Pokémon name
    pokemon_name = st.text_input("Enter a Pokémon name:")

    if st.button("Get Pokémon Info"):
        if pokemon_name:
            try:
                pokemon_data = client.get_pokemon(pokemon_name.lower())
                st.balloons()
                # Display basic information
                st.subheader(f"Information for {pokemon_data['name'].capitalize()}")
                
                st.image(pokemon_data['sprites']['front_default'], caption=pokemon_data['name'].capitalize())
                
                # Display types
                st.write("Types:")
                for type_info in pokemon_data['types']:
                    st.write(f"- {type_info['type']['name'].capitalize()}")
                
                # Display abilities
                st.write("Abilities:")
                for ability_info in pokemon_data['abilities']:
                    st.write(f"- {ability_info['ability']['name'].capitalize()}")
                
                # Display base stats
                st.write("Base Stats:")
                for stat in pokemon_data['stats']:
                    st.write(f"- {stat['stat']['name'].capitalize()}: {stat['base_stat']}")
                
            except ValueError as e:
                st.error(f"An error occurred: {e}")
                st.snow()
        else:
            st.warning("Please enter a Pokémon name.")

if __name__ == "__main__":
    main()