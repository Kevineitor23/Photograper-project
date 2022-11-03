from cgi import test
from django.urls import path
from igles.views import casa, contactoform
app_name = 'igles'

urlpatterns = [
    path('',casa, name='home'),
    path('formulario',contactoform, name='formulario')
]