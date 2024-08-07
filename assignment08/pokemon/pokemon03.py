from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

async def get_pokemon(client, url):
    print(f"{time.ctime()} - get {url}")
    resp = await client.get(url)
    pokemon_json = resp.json()
    return Pokemon(pokemon_json)

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        rand_list = [random.randint(1, 151) for _ in range(5)]
        tasks = [get_pokemon(client, f'https://pokeapi.co/api/v2/pokemon/{number}') for number in rand_list]
        pokemon_data = await asyncio.gather(*tasks)
        return pokemon_data

async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

if __name__ == '__main__':
    asyncio.run(index())
