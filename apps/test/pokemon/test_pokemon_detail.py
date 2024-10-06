import requests
import pytest
from django.test import TestCase


def detail_pokemon(search_term):
    """_summary_

    Args:
        search_term (string): id o nombre del pokemon

    Returns:
        pokemon: atributos del pokemon
    """
        
    url = 'https://pokeapi.co/api/v2/pokemon/'+search_term
    response = requests.get(url)
    payload = response.json()
        
    id = payload["id"]
    name = payload["name"]
    list_abilities = []
    for ability in payload["abilities"]:
        list_abilities.append(ability["ability"]["name"])
        
    list_type = []
    for type in payload["types"]:
        list_type.append(type["type"]["name"])
        
    list_sprites = payload["sprites"].get("back_default")
        
    return (name, list_sprites)

def test_detail_pokemon():
    """_summary_

    Args:
        search_term (string): id o nombre del pokemon

    Returns:
        pokemon: atributos del pokemon
    """
    name, list_sprites = detail_pokemon("100")
    
    assert name == "voltorb"
    assert list_sprites == "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/100.png"