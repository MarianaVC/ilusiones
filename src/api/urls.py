from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateWarehouseView,SingleWarehouseView

urlpatterns = {
	url(r'^warehouse/(?P<pk>[0-9]+)/$',
        SingleWarehouseView.as_view(), name="single"),    
    url(r'^warehouses/$', CreateWarehouseView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)