from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^neworder/$', views.neworder, name='neworder'),
    url(r'^deliver/$', views.deliver, name='deliver'),
    url(r'^deliverstatus/$', views.deliverstatus, name='deliverstatus'),
    url(r'^cancel/$', views.cancel, name='cancel'),
    url(r'^refund/$', views.refund, name='refund'),
    url(r'^exchange/$', views.exchange, name='exchange'),

    url(r'^neworders_confirm/$', views.neworder_confirm, name='neworder_confirm'),
    url(r'^deliver_confirm/$', views.deliver_confirm, name='deliver_confirm'),
    url(r'^cancel_confirm/$', views.cancel_confirm, name='cancel_confirm'),
    url(r'^cancel_deliver/$', views.cancel_deliver, name='cancel_deliver'),
    url(r'^refund_collect_done/$', views.refund_collect_done, name='refund_collect_done'),
    url(r'^refund_confirm/$', views.refund_confirm, name='refund_confirm'),
    url(r'^exchange_collect_done/$', views.exchange_collect_done, name='exchange_collect_done'),
    url(r'^exchange_confirm/$', views.exchange_confirm, name='exchange_confirm'),
]
