# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pais, Provincia, Municipio, Sujeto, Via

admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Municipio)
admin.site.register(Sujeto)
admin.site.register(Via)
