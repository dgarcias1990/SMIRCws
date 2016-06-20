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
			uri="http://wsmirc.herokuapp.com/userRoute/?usuario={0}&fecha={1}".format(data['usuario'],date.today().iso_format())
		resp={'codigo':'ruta','estatus':'ok', 'uri':uri}
	except:
		resp={'codigo':'ruta','estatus':'fallo'}

	print data
	print resp
	return HttpResponse(json.dumps(resp),content_type="application/json")

def showMap(request):

	usuario=request.GET['usuario']
	fecha=request.GET['fecha']
	instanceUser=InicioUserapp.objects.all().get(email=usuario)

	ubicaciones=list(InicioLocalization.objects.raw('select id,latitud,longitud from inicio_localization where usuario_id=%s and "fechaHora"::timestamp::date=%s group by id,latitud,longitud order by id',[instanceUser.id,fecha])) 
	
	mapsCode="""
	<script>
		var map;
      	function initMap() {
        	var mapOptions = {
          				center: new google.maps.LatLng(%s, %s),
          				zoom: 15,
          				mapTypeId: google.maps.MapTypeId.ROADMAP
        			};
        	var map = new google.maps.Map(document.getElementById("map-canvas"),mapOptions);
					"""%(ubicaciones[0].latitud,ubicaciones[0].longitud)
	
	pathElement = []
	for locate in ubicaciones:
		pathElement.append('new google.maps.LatLng(%s, %s)' % (locate.latitud, locate.longitud))
	
	pathElement = ', '.join(pathElement)
	polylineJavaScript = """var routePath = new google.maps.Polyline({path: [%s],
					strokeColor: '#FA5882',
					strokeOpacity: 1.0,
					strokeWeight: 2
					});
routePath.setMap(map);""" % (pathElement)
	
	mapsCode= mapsCode + "\n"+polylineJavaScript +"""
	}
	</script>"""
	print mapsCode

	return render(request,"RutaMaps.html",{'instancia':mapsCode})



