from django.urls import path
from app2.views import *
app_name='shinchan'
urlpatterns=[
    path('ABD/',ABD,name='ABD'),
    path('Rohit/',Rohit,name='Rohit'),
]