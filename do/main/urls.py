from django.urls import path
from . import views



urlpatterns = [

    path('do2/login', views.index, name='login'),
    path('do2/task/<int:pk>/', views.task, name='task'),
    path('do2/taske', views.taske, name='taske'),
    path('do2', views.home, name='home'),
    path('do2/account', views.account, name='account'),

]
