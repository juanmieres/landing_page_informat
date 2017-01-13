# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from . import views

urlpatterns = [

	# dashboard
	url(r'^$', views.dashboard, name='dashboard'),

	# quienes somos
	url(r'^quienes-somos/$', views.quienes_somos, name='quienes_somos'),

	# soluciones
	url(r'^soluciones/erp/$', views.soluciones_erp, name='soluciones_erp'),
	url(r'^soluciones/factura-electronica/ifacture-inet/$', views.soluciones_ifacture_inet, name='soluciones_ifacture_inet'),
	url(r'^soluciones/factura-electronica/ifacture-web/$', views.soluciones_ifacture_web, name='soluciones_ifacture_web'),
	url(r'^soluciones/sistema-control-proyecto/$', views.soluciones_control_proyecto, name='soluciones_control_proyecto'),
	url(r'^soluciones/sistema-control-locatarios/$', views.soluciones_control_locatarios, name='soluciones_control_locatarios'),
	url(r'^soluciones/business-inteligence/$', views.soluciones_business_inteligence, name='soluciones_business_inteligence'),
	url(r'^soluciones/iproperty/$', views.soluciones_iproperty, name='soluciones_iproperty'),

	# sevicios
	url(r'^servicios/consultoria/levantamiento-procesos/$', views.servicios_levantamiento_procesos, name='servicios_levantamiento_procesos'),
	url(r'^servicios/consultoria/control-proyecto/$', views.servicios_control_proyecto, name='servicios_control_proyecto'),
	url(r'^servicios/consultoria/capacitaciones/$', views.servicios_capacitaciones, name='servicios_capacitaciones'),
	url(r'^servicios/servicio-cliente/soporte/$', views.servicios_soporte, name='servicios_soporte'),
	url(r'^servicios/servicio-cliente/plataforma-tecnologica/$', views.servicios_plataforma_tecnologica, name='servicios_plataforma_tecnologica'),
	url(r'^servicios/servicio-cliente/servicio-tecnico/$', views.servicios_servicio_tecnico, name='servicios_servicio_tecnico'),

	# clientes
	url(r'^clientes/nuestros-clientes/$', views.clientes_nuestros_clientes, name='clientes_nuestros_clientes'),

	# contacto
	url(r'^contacto/$', views.contacto, name='contacto'),

]
