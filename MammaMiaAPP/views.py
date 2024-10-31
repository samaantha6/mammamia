from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Menu, Plato, Ingrediente


# Create your views here.
def index(request):
    return HttpResponse('primera vista')


def listaMenus(request):
    menus = Menu.objects.order_by('nombre')
    nombres_menus = ', '.join([menu.nombre for menu in menus])
    return HttpResponse(nombres_menus)

def detalleMENU(request, id_menu):
    try:
        menu = Menu.objects.get(pk=id_menu)
        platos = menu.platos.all()

        cadenaDeTexto = (f"Menú {menu.nombre}, "
        f"Descripcion: {menu.descripcion}, "
        f"Precio: {menu.precio}")

        if platos.exists():
            cadenaDeTexto += "Platos:\n"
            for plato in platos:
                cadenaDeTexto += f"- {plato.nombre}, Tipo: {plato.tipo}, Orden: {plato.orden}\n"
        else:
            cadenaDeTexto += "No hay platos asociados a este Menu."

        return HttpResponse(cadenaDeTexto)
    except Menu.DoesNotExist:
        return HttpResponseNotFound("Menu no encontrado")



def listaPlatos(request):
    platos = Plato.objects.order_by('nombre')
    nombres_platos = ', '.join([plato.nombre for plato in platos])
    return HttpResponse(nombres_platos)

def detallePLATO(request, id_plato):
    try:
        plato = Plato.objects.get(pk=id_plato)
        ingredientes = plato.ingredientes.all()

        cadenaDeTexto = (f"Plato {plato.nombre}, "
        f"Tipo: {plato.tipo}, "
        f"Orden: {plato.orden} ")

        if ingredientes.exists():
            cadenaDeTexto += "Ingredientes:\n"
            for ingrediente in ingredientes:
                cadenaDeTexto += f"- {ingrediente.nombre}, Alergeno: {ingrediente.alergeno}, Categoria: {ingrediente.categoria}\n"
        else:
            cadenaDeTexto += "No hay ingredientes asociados a este Plato."

        return HttpResponse(cadenaDeTexto)
    except Plato.DoesNotExist:
        return HttpResponseNotFound("Plato no encontrado")

