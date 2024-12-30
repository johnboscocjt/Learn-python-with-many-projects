# How to connect an API using python
import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokeman_info(name):
    url = f"{base_url}/pokemon/{name}"
    # method is going to return a response object
    response = requests.get(url)
    # print(response)
    
    if response.status_code == 200:
        # print("Data retrieved")
        # dictionary
        pokeman_data = response.json()
        # print(pokeman_data)
        return pokeman_data
        
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokeman_name = "pikachu"
get_pokeman_info = get_pokeman_info(pokeman_name)

if get_pokeman_info:
    print(f"Name: {get_pokeman_info["name"]}")