from django.conf.urls import include, url
from warehouses.views import *
 
urlpatterns = [
    url(r'^faker/$', upload_warehouses),
    ]