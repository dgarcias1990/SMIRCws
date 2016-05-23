from django.conf import settings
from django.conf.urls import include, url
from wsSMIRCauth.views import wsLogin, wsLocationsRegister

urlpatterns = [
    url(r'^wsLogin/$', wsLogin,name='wsLogin'),
    url(r'^wsRegisterLog/$', wsLocationsRegister,name='RegisterLogs'),
  
] 
