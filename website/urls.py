from django.urls import path
from website.views import *

app_name='website'

urlpatterns=[
    path('',website_index,name='initial'),
    path('menu/',menu_index,name='menu'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('menu-persian/',menu_index_persian,name='menu-persian'),
    path('about-persian/',about_persian,name='about-persian'),
    path('contact-persian/',contact_persian,name='contact-persian'),
]