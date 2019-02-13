# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Pais, Provincia, Municipio, Sujeto, Via
from .serializers import PaisSerializer, ProvinciaSerializer, MunicipioSerializer, SujetoSerializer, ViaSerializer

class PaisViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving paises
    """
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProvinciaViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving provincias
    """
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('pais', 'cod', )
    ordering_fields = '__all__'
    ordering = ('pais', 'cod',)


class MunicipioViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving municipios
    """
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('nom', 'provincia__nom')
    ordering_fields = '__all__'
    ordering = ('provincia', 'cod')

class SujetoViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving sujetos
    """
    queryset = Sujeto.objects.all()
    serializer_class = SujetoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ViaViewSet(viewsets.ModelViewSet):
    """
    Simple ViewSet for listing or retrieving vias
    """
    queryset = Via.objects.all()
    serializer_class = ViaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
