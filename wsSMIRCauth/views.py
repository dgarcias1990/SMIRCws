from django.shortcuts import render
from django.http import HttpResponse
from .models import InicioUserapp
import json
def wsLogin(request):
	usuario=request.GET['usuario']
	contrasena=request.GET['contrasena']
	try:
		queryset = InicioUserapp.objects.all().get(email=usuario,contrasena=contrasena)
		data={'estatus':'ok','usuario':queryset.email,'id':queryset.id}
		return HttpResponse(json.dumps(data), content_type="application/json")
	except:
		data={'estatus':'fallo'}
		return HttpResponse(json.dumps(data), content_type="application/json")
