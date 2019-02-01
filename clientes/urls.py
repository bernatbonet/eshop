# -*- encoding: utf-8 -*-
from django.conf.urls import include, url

from views import SujetoViewSet

urlpatterns = [
    url(r'^', include(SujetoViewSet)),
]
