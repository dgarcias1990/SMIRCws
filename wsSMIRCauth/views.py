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
		if queryset.sesionactiva :
			data={'codigo':'login','estatus':'ocupado'}
		else:
			InicioUserapp.objects.filter(email=usuario).update(lastlogin=datetime.now(), sesionactiva=True)
		#print timezone.localtime(timezone.now())
			data={'codigo':'login','estatus':'ok','usuario':queryset.email,'id':queryset.id}
	except:
		data={'codigo':'login','estatus':'fallo'}
	print request
	print data
	return HttpResponse(json.dumps(data), content_type="application/json")

@csrf_exempt
def wsLocationsRegister(request):
	try:
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
	except:
		resp={'codigo':'registro','estatus':'fallo'}

	print data
	print resp
	return HttpResponse(json.dumps(resp),content_type="application/json")
def wsLogout(request):
	usuario=request.GET['usuario']
	InicioUserapp.objects.filter(email=usuario).update(sesionactiva=False)
	resp={'codigo':'logout'}
	return HttpResponse(json.dumps(resp), content_type="application/json")

def wsRutaMaps(request):
	data=json.loads(request.body)
	instanceUser=InicioUserapp.objects.all().get(id=data['id'],email=data['usuario'])

	if instanceUser:
		routeCoords=[]
		for item in data['locations']:
			routeCoords.append({'lon': item['lon'], 'lat': item['lat']})

	print routeCoords

	mapasCode="""
		function initMap() {
  			var map = new google.maps.Map(document.getElementById('mapCanvas'), {
    		zoom: 12,
    		center: {lat: 0, lng: -180},
   		mapTypeId: google.maps.MapTypeId.MAPROAD
   		});
		var flightPath = new google.maps.Polyline({
    	path: [%s],
    	geodesic: true,
    	strokeColor: '#FA5882',
    	strokeOpacity: 1.0,
    	strokeWeight: 2
  		});
		flightPath.setMap(map);
		}
		"""% (routeCoords)

	return render(request,"RutasMaps.html",{'inicializar':mapasCode})

@csrf_exempt
def saveDatatoRoute(request):
	try:
		data=json.loads(request.body)
		print data
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
		resp={'codigo':'ruta','estatus':'ok'}
	except:
		resp={'codigo':'ruta','estatus':'fallo'}

	print data
	print resp
	return HttpResponse(json.dumps(resp),content_type="application/json")

