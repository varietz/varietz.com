from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from varietz_fs.views import *


urlpatterns = [
    url(r'^$', Base),
    url(r'^userpage/$', UserBaseView),
    url(r'^contactus/$', contactus),
    url(r'^aboutus/$', aboutus),
    url(r'^careers/$', careers),
    url(r'^terms12/$', terms12),
    url(r'^LoadFashionPage/$', LoadFashionPage),
    url(r'^LoadElectronicsPage/$', LoadElectronicsPage),
    url(r'^LoadAppliancesPage/$', LoadAppliancesPage),
    url(r'^getImgPriceHis/$', getImgPriceHis),
    url(r'^login/$', login),
]
