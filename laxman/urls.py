from django.urls import path
from laxman.views import *
app_name='hello'
urlpatterns=[
    path('fn_laxman/',fn_laxman,name='fn_laxman'),
]