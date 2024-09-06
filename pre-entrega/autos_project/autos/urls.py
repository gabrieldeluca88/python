from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_modelo/', views.agregar_modelo, name='agregar_modelo'),
    path('agregar_auto/', views.agregar_auto, name='agregar_auto'),
    path('buscar/', views.buscar, name='buscar'),
]
