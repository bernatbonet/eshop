# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models

class Meta:
	verbose_name = _(u'Clientes')

class Via(models.Model):
	"""
	Type of road model
	"""
	cod5 = models.CharField(max_length=5, verbose_name = _(
		u'Codigo Largo'), help_text= _(u'Introduzca el codigo largo de via'), unique=True)
	cod2 = models.CharField(max_length=2, verbose_name = _(
		u'Codigo Corto'), help_text= _(u'Introduzca el codigo corto de via'))
	desc = models.CharField(max_length=35, verbose_name= _(
		u'Descripcion'), help_text= _(u'Introduzca la descripcion de la via'), unique=True)

	def __unicode__(self):
		return u'{} - {}'.format(self.cod2, self.desc)
	
	def __str__(self):
		return '{} - {}'.format(self.cod2, self.desc)

	class Meta:
		verbose_name = _('Via')
		verbose_name_plural = _('Vias')

class Provincia(models.Model):
	"""
	States model
	"""
	pais = models.ForeignKey('Pais', on_delete=models.CASCADE, 
		verbose_name = _(u'Pais'), help_text= _(u'Introduzca el país al que pertenece la provincia'))
	cod = models.CharField(max_length=2, verbose_name = _(
		u'Codigo'), help_text= _(u'Introduzca el codigo de provincia'), unique=True)
	nom = models.CharField(max_length=60, verbose_name= _(
		u'Nombre'), help_text= _(u'Introduzca el nombre de la provincia'), unique=True)

	def __unicode__(self):
		return u'{} - {}'.format(self.cod, self.nom)
	
	def __str__(self):
		return '{} - {}'.format(self.cod, self.nom)

	class Meta:
		verbose_name = _('Provincia')
		verbose_name_plural = _('Provincias')

class Pais(models.Model):
	"""
	Worldwide countries
	"""
	nom = models.CharField(max_length=60, verbose_name= _(
		u'Nombre'), help_text= _(u'Introduzca el nombre del país'))
	alfa2 = models.CharField(max_length=2, verbose_name= _(
		u'Alfa-2'), help_text= _(u'Introduzca el código alfa 2 del país'))
	alfa3 = models.CharField(max_length=3, verbose_name= _(
		u'Alfa-3'), help_text= _(u'Introduzca el código alfa 3 del país'))
	cod = models.CharField(max_length=3, verbose_name= _(
		u'Numerico'), help_text= _(u'Introduzca el código numérico del país'), unique=True)

	def __unicode__(self):
		return u'{}'.format(self.nom)
	
	def __str__(self):
		return '{}'.format(self.nom)

	class Meta:
		verbose_name = _('Pais')
		verbose_name_plural = _('Paises')

class Municipio(models.Model):
	"""
	States model
	"""
	provincia = models.ForeignKey('Provincia', on_delete=models.CASCADE, 
		verbose_name = _(u'Provincia'), help_text= _(u'Introduzca la provincia al que pertenece el municipio'))
	cod = models.CharField(max_length=3, verbose_name = _(
		u'Codigo'), help_text= _(u'Introduzca el codigo de municipio'), unique=True)
	nom = models.CharField(max_length=60, verbose_name= _(
		u'Nombre'), help_text= _(u'Introduzca el nombre del municipio'), unique=True)

	def __unicode__(self):
		return u'{} - {}'.format(self.cod, self.nom)
	
	def __str__(self):
		return '{} - {}'.format(self.cod, self.nom)

	class Meta:
		verbose_name = _('Municipio')
		verbose_name_plural = _('Municipios')

class Sujeto(models.Model):
	"""
	Subject type
	"""
	cod = models.CharField(max_length=3, verbose_name=_(
		u'Código'), help_text=_(u'Introduzca el código'), unique=True)
	nom = models.CharField(max_length=100, verbose_name=_(
		u'Nombre'), help_text=_(u'Introduzca el nombre'), unique=True)
	formasocial = models.CharField(max_length=10, verbose_name=_(
		u'Forma Social'), help_text=_(u'Introduzca la forma social'), null=True, blank=True)

	def __unicode__(self):
		return self.nom
	
	def __str__(self):
    		return "{} - {}".format(self.cod, self.nom)

	class Meta:
		verbose_name = _(u'Sujeto')
		verbose_name_plural = _(u'Sujetos')
