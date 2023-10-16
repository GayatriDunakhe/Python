from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('show/', views.show, name='show'),
    path('name/', views.name_list, name='name_list'),
    path('numbers/', views.num_list, name='num_list'),
    path('age/', views.agecheck, name='agecheck')
]