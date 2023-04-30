from django.urls import path

from .views import index,about,blog,contact,service


urlpatterns = [
    path('',index,name='home'),
    path('about',about,name='about'),
    path('blog',blog,name='blog'),
    path('contactus', contact, name='contact'),
    path('service', service, name='service')
]