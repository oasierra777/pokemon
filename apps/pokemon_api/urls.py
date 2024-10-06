from django.urls import path

from apps.pokemon_api.views import ListPokemonApiView
from apps.pokemon_api.views import DetailIDPokemonApiView
from apps.pokemon_api.views import UpdatePokemonApiView

urlpatterns = [
    #las diferentes urls para la app de pokemon
    path('', ListPokemonApiView.as_view()),
    path("search/<str:search_term>", DetailIDPokemonApiView.as_view()),
    path("update/<str:update_term>", UpdatePokemonApiView.as_view()),
    
]
