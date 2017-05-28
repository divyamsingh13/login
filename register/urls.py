from django.conf.urls import url
from register import views
import django.contrib.auth.views
urlpatterns=[
    #url(r'^$',views.mainpage,name='mainpage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/',views.logout_page,name='logout'),
    url(r'^login/$', django.contrib.auth.views.login,name='login'),
]