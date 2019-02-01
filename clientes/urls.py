# -*- encoding: utf-8 -*-
from django.conf.urls import include, url

from views import SujetoList, SujetoDetail

sujeto_urls = patterns('',
                    url(r'^(?P<cod>[0-9a-zA-Z]+)/',
                        SujetoDetail.as_view(), name='sujeto-detail'),
                    url(r'^', SujetoList.as_view(), name='sujeto-list'),
                    )


"""urlpatterns = urlpatterns[]
    'clientes.views', url(r'^sujeto/', include(sujeto_urls)),
]"""
