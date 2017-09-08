from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^neworder/$', views.neworder, name='neworder'),
    url(r'^todeliver/$', views.todeliver, name='todeliver'),
    url(r'^sending/$', views.sending, name='sending'),
    url(r'^tocancel/$', views.tocancel, name='tocancel'),
    url(r'^toreturn/$', views.toreturn, name='toreturn'),
    url(r'^toexchange/$', views.toexchange, name='toexchange'),

    url(r'^neworders_confirm/$', views.neworder_confirm, name='neworder_confirm'),
    url(r'^todeliver_confirm/$', views.todeliver_confirm, name='todeliver_confirm'),
    url(r'^tocancel_confirm/$', views.tocancel_confirm, name='tocancel_confirm'),
    url(r'^tocancel_deliver/$', views.tocancel_deliver, name='tocancel_deliver'),
    url(r'^toreturn_confirm/$', views.toreturn_confirm, name='toreturn_confirm'),
    url(r'^toexchange_confirm/$', views.toexchange_confirm, name='toexchange_confirm'),
]
