from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listaM'),
    path('listadoDeMenus/', views.listaMenus, name='listaM'),
    path('menus/<int:id_menu>/', views.detalleMENU, name='detalle'),

    path('listadoDePlatos/', views.listaPlatos, name='listaP'),
    path('platos/<int:id_plato>/', views.detallePLATO, name='detalle')
]

