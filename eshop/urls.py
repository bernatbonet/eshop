"""eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, re_path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from clientes import views as clientes_views 

router = routers.DefaultRouter()
router.register(r'paises', clientes_views.PaisViewSet,  basename='paises')
router.register(r'provincias', clientes_views.ProvinciaViewSet,  basename='provincias')
router.register(r'sujetos', clientes_views.SujetoViewSet,  basename='sujetos')
router.register(r'vias', clientes_views.ViaViewSet,  basename='vias')

from clientes import urls as urls_clientes

urlpatterns = [
<<<<<<< HEAD
    url(r'^clientes/', include(urls_clientes)),
    url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
=======
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
>>>>>>> b3c9a43a39b8e3021ddea700f30e39f5a8dcd9bd
]

urlpatterns += staticfiles_urlpatterns()

from .settings import development

if development.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
