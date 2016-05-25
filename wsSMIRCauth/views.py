from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import InicioUserapp,InicioLocalization
from datetime import datetime,date,time,timedelta
#from django.utils import timezone, dateparse
from django.utils.timezone import get_current_timezone
import string
import json
def wsLogin(request):
	usuario=request.GET['usuario']
	contrasena=request.GET['contrasena']
	try:
		queryset = InicioUserapp.objects.all().get(email=usuario,contrasena=contrasena)
		InicioUserapp.objects.filter(email=usuario).update(lastlogin=datetime.now())
		# print timezone.localtime(timezone.now())
		data={'codigo':'login','estatus':'ok','usuario':queryset.email,'id':queryset.id}
	except:
		data={'codigo':'login','estatus':'fallo'}
	return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def wsLocationsRegister(request):
	# try:
	data=json.loads(request.body)
	instanceUser=InicioUserapp.objects.all().get(id=data['id'],email=data['usuario'])
	for item in data['locations']:
		instance=InicioLocalization()
		instance.usuario=instanceUser
		instance.latitud=item['lat']
		instance.longitud=item['lon']
		instance.altitud=item['alto']
		instance.charla=item['voz']
		instance.fechahora=item['hora']
		#instance.fechaHora=datetime.strptime("'"+item["hora"]+"'", ))
		#instance.fechaHora=parse_datetime(item['hora'])
		print instance.fechahora
		instance.save()
	resp={'codigo':'registro','estatus':'ok'}
	# except:
	# resp={'codigo':'registro','estatus':'fallo'}

	return HttpResponse(json.dumps(resp),content_type="application/json")