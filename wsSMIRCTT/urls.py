from django.conf import settings
from django.conf.urls import include, url
from wsSMIRCauth.views import wsLogin, wsLocationsRegister,wsLogout,showMap,saveDatatoRoute

urlpatterns = [
    url(r'^wsLogin/$', wsLogin,name='wsLogin'),
    url(r'^wsRegisterLog/$', wsLocationsRegister,name='RegisterLogs'),
    url(r'^wsLogout/$', wsLogout,name='Logout'),
    url(r'^userRoute/$',showMap, name='ruta'),
    url(r'^wsrutaUsuario/$',saveDatatoRoute,name="rutaUsuario"),
] 
