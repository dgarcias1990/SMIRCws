from django.conf import settings
from django.conf.urls import include, url
from wsSMIRCauth.views import wsLogin

urlpatterns = [
    url(r'^wsLogin/$', wsLogin,name='hola'),
  
] 
