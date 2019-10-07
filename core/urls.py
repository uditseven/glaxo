from django.urls import path
from . import views

urlpatterns ={

<<<<<<< HEAD
    path('', views.base, name='base'),
    path('index/', views.index, name='index'),
=======
    path('', views.index, name='index'),
    path('shubham/',views.inventory,name='inventory'),
>>>>>>> 67d417ebeb68daf6033828affe4db63efb8e6c65
    
}


