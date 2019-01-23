"""ilusiones URL Configuration
"""
from django.conf.urls import url,include
from django.contrib import admin
from ajax_select import urls as ajax_select_urls

admin.site.site_header = "Ilusiones Admin"
admin.site.site_title = "Ilusiones Admin Portal"
admin.site.index_title = "Welcome to the Ilusiones Admin Portal"


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS    
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_select/', include(ajax_select_urls)),
]
