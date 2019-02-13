# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Pais, Provincia, Municipio, Sujeto, Via
from .serializers import PaisSerializer, ProvinciaSerializer, MunicipioSerializer, SujetoSerializer, ViaSerializer

class PaisViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving paises
    """
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [AllowAny]

class ProvinciaViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving provincias
    """
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    permission_classes = [AllowAny]


class MunicipioViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving municipios
    """
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [AllowAny]

class SujetoViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving sujetos
    """
    queryset = Sujeto.objects.all()
    serializer_class = SujetoSerializer
    permission_classes = [AllowAny]

class ViaViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving vias
    """
    queryset = Via.objects.all()
    serializer_class = ViaSerializer
    permission_classes = [AllowAny]
