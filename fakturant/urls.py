from django.conf.urls import url

from . import views

app_name = 'fakturant'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<company_short_name>[\w.@+-]+)/$', views.show_company, name='show_company'),
    url(r'^invoice/(?P<invoice_id>[0-9]+)$', views.show_invoice, name='show_invoice')
]