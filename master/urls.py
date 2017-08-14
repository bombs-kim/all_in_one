from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout, logout_then_login

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),

    url(r'^register/$', views.register, name='register'),
    # url(r'^edit/$', views.edit, name='edit'),

    # login / logout urls
    url(r'^login/$', login,
        {'template_name': 'custom_registration/login.html'},
        name='login'),
    url(r'^logout/$', logout,
        {'template_name': 'custom_registration/logged_out.html'},
        name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

    # Change password urls
    # url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    # url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),

    # Restore password urls
    # url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    # url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    # url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]
