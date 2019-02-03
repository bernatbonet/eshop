# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Sujeto
from .serializers import SujetoSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'sujetos': reverse('sujetos-list', request=request, format=format),
    })

class SujetoList(generics.ListCreateAPIView):
    queryset = Sujeto.objects.all()
    serializer_class = SujetoSerializer
    permission_classes = (permissions.IsAuthenticated,) 

class SujetoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sujeto.objects.all()
    serializer_class = SujetoSerializer
    permission_classes = (permissions.IsAuthenticated,) 