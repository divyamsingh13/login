from django.conf.urls import url,include
from django.contrib import admin
from register import urls
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^',include('register.urls')),
]
