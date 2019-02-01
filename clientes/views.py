# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from models import Sujeto
from serializers import SujetoSerializer


class SujetoViewSet(viewsets.ModelViewSet):
    serializer_class = SujetoSerializer
