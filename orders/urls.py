from django.conf.urls import url
from django.urls import include
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'paypal/', include('paypal.standard.ipn.urls')),
]
