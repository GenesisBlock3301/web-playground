from django.urls import path
from . import views

urlpatterns = [
    path('',views.TodoList.as_view(),name='todos-list-url'),
    path('<str:id>/completed/', views.TodoCompleted.as_view(), name='todos-completed-url'),
    path('<str:id>/deleted/', views.TodoDeleted.as_view(), name='todos-deleted-url'),
]
