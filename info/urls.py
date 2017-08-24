from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^neworder/$', views.neworder, name='neworder'),
    url(r'^neworders_confirm/$', views.neworder_confirm, name='neworder_confirm'),
    url(r'^todeliver/$', views.todeliver, name='todeliver'),
    url(r'^todeliver_confirm/$', views.todeliver_confirm, name='todeliver_confirm'),
    url(r'^sending/$', views.sending, name='sending'),
]
