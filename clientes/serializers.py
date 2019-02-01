
#-*- coding: utf-8 -*-
from models import Sujeto
from rest_framework import serializers


class SujetoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sujeto
		fields = ('cod', 'nom', 'formasocial', )
