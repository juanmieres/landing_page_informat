from django.shortcuts import render

# dashboard
def dashboard(request):
	return render(request, 'dashboard.html')


# quienes somos
def quienes_somos(request):
	return render(request, 'quienes_somos.html')


# soluciones
def soluciones_erp(request):
	return render(request, 'pages/soluciones/erp.html')

def soluciones_ifacture_inet(request):
	return render(request, 'pages/soluciones/ifacture_inet.html')

def soluciones_ifacture_web(request):
	return render(request, 'pages/soluciones/ifacture_web.html')

def soluciones_control_proyecto(request):
	return render(request, 'pages/soluciones/control_proyecto.html')

def soluciones_control_locatarios(request):
	return render(request, 'pages/soluciones/control_locatarios.html')

def soluciones_business_inteligence(request):
	return render(request, 'pages/soluciones/business_inteligence.html')

def soluciones_iproperty(request):
	return render(request, 'pages/soluciones/iproperty.html')


# sevicios
def servicios_levantamiento_procesos(request):
	return render(request, 'pages/servicios/levantamiento_procesos.html')

def servicios_control_proyecto(request):
	return render(request, 'pages/servicios/control_proyecto.html')

def servicios_capacitaciones(request):
	return render(request, 'pages/servicios/capacitaciones.html')

def servicios_soporte(request):
	return render(request, 'pages/servicios/soporte.html')

def servicios_plataforma_tecnologica(request):
	return render(request, 'pages/servicios/plataforma_tecnologica.html')

def servicios_servicio_tecnico(request):
	return render(request, 'pages/servicios/servicio_tecnico.html')


# clientes
def clientes_nuestros_clientes(request):
	return render(request, 'pages/clientes/nuestros_clientes.html')


# contacto
def contacto(request):
	return render(request, 'pages/contacto/contacto.html')

