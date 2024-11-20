const PokeAPIClient = require('../sdk/pokeApiClient');

const client = new PokeAPIClient();

describe('PokeAPIClient', () => {
    it('fetches a Pokémon by name', async () => {
        const pokemon = await client.getPokemon('pikachu');
        expect(pokemon.name).toBe('pikachu');
    });

    it('fetches a generation by ID', async () => {
        const generation = await client.getGeneration(1);
        expect(generation.name).toBe('generation-i');
    });

    it('fetches paginated results', async () => {
        const endpoint = '/pokemon';

        // Mock API response
        const mockResponse = {
            count: 100,
            results: [
                { name: 'bulbasaur' },
                { name: 'ivysaur' },
                { name: 'venusaur' },
            ],
        };

        // Mock axios request
        jest.spyOn(client.api, 'get').mockResolvedValueOnce({ data: mockResponse });

        const results = await client.getPaginatedResults(endpoint, 3, 0);

        expect(results.count).toBe(100);
        expect(results.results.length).toBe(3);
        expect(results.results[0].name).toBe('bulbasaur');
    });
});
