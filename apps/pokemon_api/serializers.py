from rest_framework import serializers


class PokemonApiSerializer(serializers.Serializer):

    class Meta:       
        fields = '__all__'
