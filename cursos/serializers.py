from dataclasses import fields
from rest_framework import serializers
from .models import Curso, Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {'email': {'write_only': True}} #Email é um campo sensível, eu preciso dele para o POST, mas nao deve ser exibido no GET
        model = Avaliacao
        fields = '__all__'
        
    def validate_avaliacao(self, valor):
        if valor in range(1, 6):
            return valor
        raise serializers.ValidationError("A avaliação precisa ser um inteiro entre 1 e 5")


class CursoSerializer(serializers.ModelSerializer):
    
    #Nested relationship
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)
    
    #HyperLinked Related Field
    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')
    
    # Primary Key Related Field
    avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Curso
        fields = '__all__'
