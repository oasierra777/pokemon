import requests
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
 
from apps.pokemon_api.serializers import PokemonApiSerializer

class ListPokemonApiView(APIView):
    """_summary_

    Args:
        APIView : vista general

    Returns:
        la lista de los pokemons
    """
    serializer_class = PokemonApiSerializer
    
    def get(self, request):
        """_summary_

        Args:
            request: realliza la solicitud a la api pokeapi

        Returns:
            lista: lista de los pokemons
        """
        url = 'https://pokeapi.co/api/v2/pokemon'
        response = requests.get(url)
        try:
            payload = response.json()
            list_results = []
            for result in payload["results"]:
                list_results.append("name "+result["name"]+" url "+result["url"])

            return Response({
                'results':list_results,
                }, status=status.HTTP_200_OK)
        except:
            return Response(
                {'error': 'No es la la url correcta'},
                status=status.HTTP_404_NOT_FOUND
            )

                
class DetailIDPokemonApiView(APIView):
    """_summary_

    Args:
        APIView : vista general para detallar el pokemon

    Returns:
        pokemon: un objeto pokemon
    """
    serializer_class = PokemonApiSerializer
    
    def get(self,request,search_term):
        """_summary_

        Args:
            request: realliza la solicitud a la api pokeapi por medio del id o el nomre del pokemon

        Returns:
            pokemon: pokemon con los taributos id, name, lista de habilidades, lista de tipos
        """
        
        url = 'https://pokeapi.co/api/v2/pokemon/'+search_term
        response = requests.get(url)
        try:
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

   
            return Response({
                    'name':name,
                    'abilities':list_abilities,
                    'id': id,
                    'types':list_type,
                    'sprites':list_sprites,
                }, status=status.HTTP_200_OK)
        except:
            return Response(
                {'error': 'el pokedex o el nombre no es correcto'},
                status=status.HTTP_404_NOT_FOUND
            )
            
class UpdatePokemonApiView(generics.UpdateAPIView):
    """_summary_

        Args:
            request: realliza la solicitud a la api pokeapi por medio del id o nombre del pokemon

        Returns:
            pokemon: ,odificado
        """
    serializer_class = PokemonApiSerializer
    
    def get_queryset(self, update_term):
        """_summary_

        Args:
            request: realliza la solicitud a la api pokeapi

        Returns:
            pokemon: pokemon modificado en los atributos
        """
        url = 'https://pokeapi.co/api/v2/pokemon/'+update_term
        response = requests.get(url)
        payload = response.json()
        print(payload)
        return self.get_serializer()

            
    def patch(self, request, update_term = None):
        if self.get_queryset(update_term):
            pokemon_serializer = self.serializer_class(self.get_queryset(update_term))
            print(pokemon_serializer.data)
            return Response(pokemon_serializer.data, status= status.HTTP_200_OK)
        return Response({'error': 'No es la la url correcta'},
                status=status.HTTP_404_NOT_FOUND
            )
        
    def put(self, request, update_term=None):
        if self.get_queryset(update_term):
            pokemon_serializer = self.serializer_class(self.get_queryset(update_term), data=request.data)
            if pokemon_serializer.is_valid():
                print(pokemon_serializer.data)
                return Response(pokemon_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No es la la url correcta'},
                status=status.HTTP_404_NOT_FOUND
            )