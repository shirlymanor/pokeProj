const axios = require('axios');

class PokeAPIClient {
    /**
     * Initializes the API client with a base URL.
     * @param {string} baseURL - The base URL of the PokeAPI.
     */
    constructor(baseURL = 'https://pokeapi.co/api/v2') {
        this.api = axios.create({
            baseURL,
            timeout: 5000, // Optional timeout setting for requests
        });
    }

    /**
     * Fetches details of a Pokémon by its ID or name.
     * @param {string|number} idOrName - The ID or name of the Pokémon.
     * @returns {Promise<object>} - Pokémon details as an object.
     */
    async getPokemon(idOrName) {
        try {
            const response = await this.api.get(`/pokemon/${idOrName}`);
            return response.data;
        } catch (error) {
            console.error(`Error fetching Pokémon with ID/Name '${idOrName}':`, error.message);
            throw new Error(`Unable to fetch Pokémon data for ${idOrName}`);
        }
    }

    /**
     * Fetches details of a generation by its ID or name.
     * @param {string|number} idOrName - The ID or name of the generation.
     * @returns {Promise<object>} - Generation details as an object.
     */
    async getGeneration(idOrName) {
        try {
            const response = await this.api.get(`/generation/${idOrName}`);
            return response.data;
        } catch (error) {
            console.error(`Error fetching Generation with ID/Name '${idOrName}':`, error.message);
            throw new Error(`Unable to fetch Generation data for ${idOrName}`);
        }
    }

    /**
     * Generic method to fetch paginated results.
     * @param {string} endpoint - API endpoint to fetch paginated data.
     * @param {number} [limit=20] - Number of items per page.
     * @param {number} [offset=0] - The offset for pagination.
     * @returns {Promise<object>} - Paginated results from the API.
     */
    async getPaginatedResults(endpoint, limit = 20, offset = 0) {
        try {
            const response = await this.api.get(endpoint, {
                params: { limit, offset },
            });
            return response.data;
        } catch (error) {
            console.error(`Error fetching paginated results from '${endpoint}':`, error.message);
            throw new Error(`Unable to fetch data from ${endpoint}`);
        }
    }
}

module.exports = PokeAPIClient;
