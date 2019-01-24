from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateWarehouseView,SingleWarehouseView,SingleProductView,CreateProductView,CreatePurchaseOrderCSVView,CreatePurchaseOrderView,SinglePurchaseOrderCSVView,SinglePurchaseOrderView

urlpatterns = {
	url(r'^warehouse/(?P<pk>[0-9]+)/$',
        SingleWarehouseView.as_view(), name="warehouse"),    
    url(r'^warehouses/$', CreateWarehouseView.as_view(), name="warehouses"),
    url(r'^product/(?P<pk>[0-9]+)/$', SingleProductView.as_view(), name="product"),
    url(r'^products/$', CreateProductView.as_view(), name="products"),
    url(r'^order/(?P<warehouse_id>[0-9]+)/$', SinglePurchaseOrderView.as_view(), name="order"),
    url(r'^orders/$', CreatePurchaseOrderCSVView.as_view(), name="orders"),
    url(r'^order_csv/(?P<pk>[0-9]+)/$', SinglePurchaseOrderCSVView.as_view(), name="csv"),
    url(r'^order_csvs/$', CreatePurchaseOrderCSVView.as_view(), name="csvs"),

}

urlpatterns = format_suffix_patterns(urlpatterns)