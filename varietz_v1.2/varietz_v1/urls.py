from django.conf.urls import include, url
from django.contrib import admin
from varietz_fs.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
	url(r'^base/', include('varietz_fs.urls')),

]