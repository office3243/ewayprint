from django.conf.urls import url
from django.contrib.auth.views import LoginView, logout_then_login
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='portal/login.html'), name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),

    url(r'^transaction/add/$', views.transaction_add, name='transaction_add'),
    url(r'^transaction/otp_generated/(?P<otp_1>[0-9]+)/(?P<otp_2>[0-9]+)/$', views.otp_generated, name='otp_generated'),

    url(r'^get_print/(?P<otp_1>[0-9]+)/(?P<otp_2>[0-9]+)/$', views.get_print, name='get_print'),

]
