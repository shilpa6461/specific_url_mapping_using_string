from django.urls import path
from app1.views import *
app_name='nothing'
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
    path('virat/',virat,name='virat'),
]