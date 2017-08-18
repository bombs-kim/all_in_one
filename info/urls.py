from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^neworders/$', views.neworders, name='neworders'),
    url(r'^todeliver/$', views.todeliver, name='todeliver'),
    url(r'^sending/$', views.sending, name='sending'),
]
