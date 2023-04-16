import asyncio
from random import randint
import json

JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
import requests
import aiohttp

MAX_POKEMONID = 898
JSONObject = dict[str, JSON]


def my_request(url):
    resp = requests.get(url)
    return str(resp.json()["abilities"][0]["ability"]["name"])


async def http_get(url: str) -> JSONObject:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


def get_pokemon_name_sync():
    pokemon_id = randint(1, MAX_POKEMONID)
    pokenmon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = my_request(pokenmon_url)
    return pokemon


async def get_pokemon_name():
    pokemon_id = randint(1, MAX_POKEMONID)
    pokenmon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokenmon_url)
    return pokemon['name']


async def main():
    # for _ in range(20):
    #     pokemon_name = await get_pokemon_name()
    #     print(pokemon_name['name']) 

    result = await asyncio.gather(*[get_pokemon_name() for _ in range(20)])
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
