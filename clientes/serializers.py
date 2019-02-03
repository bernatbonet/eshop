#-*- encoding: utf-8 -*-
from rest_framework import serializers
from .models import Sujeto

class SujetoSerializer(serializers.ModelSerializer):
    	
	class Meta:
		model = Sujeto
		fields = ('cod', 'nom', 'formasocial', )
