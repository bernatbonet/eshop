#-*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Pais, Provincia, Municipio, Sujeto, Via

class PaisSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = Pais
		fields = ('id', 'nom', 'alfa2', 'alfa3', 'cod', )

class ProvinciaSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = Provincia
		fields = ('pais', 'cod', 'nom', )

class MunicipioSerializer(serializers.ModelSerializer):
    
	class Meta:
		model = Municipio
		fields = ('provincia', 'cod', 'nom', )

class SujetoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Sujeto
		fields = ('cod', 'nom', 'formasocial', )

class ViaSerializer(serializers.ModelSerializer):

	class Meta:
		model = Via
		fields = ('cod5', 'cod2', 'desc', )
