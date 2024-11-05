from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('listadoDeMenus/', views.listaMenus, name='listaM'),
    path('listaMENUConPlantillas/', views.listaMENUConPlantillas, name='listaMENUConPlantillas'),
    path('detalleMENUConPlantillas/<int:id_menu>/', views.detalleMENUConPlantillas, name='detalleMENUConPlantillas'),
    path('menus/<int:id_menu>/', views.detalleMENU, name='detalle'),

    path('listadoDePlatos/', views.listaPlatos, name='listaP'),
    path('listaPLATOConPlantillas/', views.listaPLATOConPlantillas, name='listaPLATOConPlantillas'),
    path('detallePLATOConPlantillas/<int:id_plato>/', views.detallePLATOConPlantillas, name='detallePLATOConPlantillas'),
    path('platos/<int:id_plato>/', views.detallePLATO, name='detalle'),

    path('listadoDeIngredientes/', views.listaIngredientes, name='listaE'),
    path('listaINGREDIENTEConPlantillas/', views.listaINGREDIENTEConPlantillas, name='listaINGREDIENTEConPlantillas'),
    path('detalleINGREDIENTEConPlantillas/<int:id_ingrediente>', views.detalleINGREDIENTEConPlantillas, name='detalleINGREDIENTEConPlantillas'),
    path('ingredientes/<int:id_ingrediente>/', views.detalleINGREDIENTE, name='detalle')
]

