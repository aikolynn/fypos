from django.conf.urls import patterns, include, url
from django.contrib import admin
from oldfypos.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^exportxls/',export_xls,name='exportxls'),
    url(r'^$',sale_flow,name='saleflow')
)
