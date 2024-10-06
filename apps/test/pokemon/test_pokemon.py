import requests
import pytest
from django.test import TestCase

@pytest.fixture
def list_pokemon():
        
        url = 'https://pokeapi.co/api/v2/pokemon'
        response = requests.get(url)
        payload = response.json()
        list_results_name = []
        for result in payload["results"]:
            list_results_name.append(result["name"])
        
        return list_results_name


def test_list_pokemon(list_pokemon):
    size_response = len(list_pokemon)
    name_5 = list_pokemon[5]
    name_19 = list_pokemon[19]
    assert size_response == 20
    assert name_5 == "charizard"
    assert name_19 == "raticate"