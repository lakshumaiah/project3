from django.urls import path
from ram.views import *
app_name='hi'
urlpatterns=[
    path('fn_ram/',fn_ram,name='fn_ram'),
]