from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search_emp, name='search'),
    path('create/', views.create_emp, name='create'),
    path('delete/<str:pk>/', views.delete_emp, name='delete'),
    path('update/<str:pk>/', views.update_emp, name='update'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]