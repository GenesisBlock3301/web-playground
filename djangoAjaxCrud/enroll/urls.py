from django.urls import path
from .views import *

urlpatterns = [

    path('', home, name="home"),
    path('save/',save_data, name="save_data"),
    path('delete/',delete_data, name="delete_data"),
    path('edit/',edit_data, name="edit_data"),
]
