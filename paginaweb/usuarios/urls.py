from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('single', views.single, name='single'),
    
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/crear', views.crear, name='crear'),
    path('usuarios/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('usuarios/editar/<int:id>', views.editar, name='editar'),
    
   
]
