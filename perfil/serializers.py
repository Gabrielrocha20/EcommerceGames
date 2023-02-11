from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Perfil


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = [
                "idade", "data_nascimento", "cpf", "endereco",
                "numero", "complemento", "bairro",
                "cep", "cidade", "estado"
            ]