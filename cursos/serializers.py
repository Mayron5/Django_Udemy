from dataclasses import fields
from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {'email': {'write_only': True}} #Email é um campo sensível, eu preciso dele para o POST, mas nao deve ser exibido no GET
        model = Avaliacao
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'
