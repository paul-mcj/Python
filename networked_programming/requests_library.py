# The use of the "requests" third-party library easily allows for https communications
import requests
import json

def main():
    base_url = "https://pokeapi.co/api/v2/pokemon/"

    def get_pokemon_info(name):
        target_url = f"{base_url}{name}"
        res = requests.get(target_url)

        if res.status_code == 200:
            found = json.dumps(res.json(), indent=4, sort_keys=True)
            return found

        else:
            print(f"Failed to retrieve data for pokemon {name} -- Response [{res.status_code}]")

    pokemon_name = "raichu"

    fetch_pokemon = get_pokemon_info(pokemon_name)

    print(fetch_pokemon)
    

if __name__ == "__main__":
    main()