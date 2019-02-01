# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models


class Sujeto(models.Model):
	cod = models.CharField(max_length=3, verbose_name=_(
		u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(
		u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)
	formasocial = models.CharField(max_length=10, verbose_name=_(
		u'Forma Social'), help_text=_(u'Introduzca la forma social'), null=True, blank=True)

	def __unicode__(self):
		return self.nom

	class Meta:
		verbose_name = _(u'Sujeto')
		verbose_name_plural = _(u'Sujetos')
