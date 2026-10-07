from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_objetos, name='listar_objetos'),
    path('nuevo/', views.crear_objeto, name='crear_objeto'),
    path('editar/<int:id>/', views.editar_objeto, name='editar_objeto'),
    path('eliminar/<int:id>/', views.eliminar_objeto, name='eliminar_objeto'),
]

