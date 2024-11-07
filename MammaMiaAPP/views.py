from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .models import Menu, Plato, Ingrediente


# Create your views here.
def index(request):
    return render(request, 'index.html')


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
        f"Orden: {plato.orden}")

        if ingredientes.exists():
            cadenaDeTexto += "Ingredientes:\n"
            for ingrediente in ingredientes:
                cadenaDeTexto += f"- {ingrediente.nombre}, Alergeno: {ingrediente.alergeno}, Categoria: {ingrediente.categoria}\n"
        else:
            cadenaDeTexto += "No hay ingredientes asociados a este Plato."

        return HttpResponse(cadenaDeTexto)
    except Plato.DoesNotExist:
        return HttpResponseNotFound("Plato no encontrado")

def listaIngredientes(request):
    ingredientes = Ingrediente.objects.all()
    cadenaDeTexto = "Lista de ingredientes:\n"

    if ingredientes.exists():
        for ingrediente in ingredientes:
            cadenaDeTexto += (
                f"- ID: {ingrediente.id}, "
                f"Nombre: {ingrediente.nombre}, "
                f"Alergeno: {ingrediente.alergeno}, "
                f"Categoria: {ingrediente.categoria}, "
                f"Plato: {ingrediente.plato.nombre}\n"
            )
    else:
        cadenaDeTexto += "No hay ingredientes registrados."
    return HttpResponse(cadenaDeTexto)

def detalleINGREDIENTE(request, id_ingrediente):
    try:
        ingrediente = Ingrediente.objects.get(pk=id_ingrediente)

        cadenaDeTexto = (f"Ingrediente {ingrediente.nombre}, "
        f"Alergeno: {ingrediente.alergeno}, "
        f"Categoria: {ingrediente.categoria}")

        return HttpResponse(cadenaDeTexto)
    except Plato.DoesNotExist:
        return HttpResponseNotFound("Ingrediente no encontrado")

def detalleMENUConPlantillas(request, id_menu):
    menu = get_object_or_404(Menu, pk=id_menu)
    contexto = {'menu': menu}
    return render(request, 'detalleM.html', contexto)

def listaMENUConPlantillas(request):
    menus = Menu.objects.order_by('nombre')
    contexto = {'lista_menus': menus}
    return render(request, 'listaM.html', contexto)

def detallePLATOConPlantillas(request, id_plato):
    plato = get_object_or_404(Plato, pk=id_plato)
    contexto = {'plato': plato}
    return render(request, 'detalleP.html', contexto)

def listaPLATOConPlantillas(request):
    platos = Plato.objects.order_by('nombre')
    contexto = {'lista_platos': platos}
    return render(request, 'listaP.html', contexto)

def detalleINGREDIENTEConPlantillas(request, id_ingrediente):
    ingrediente = get_object_or_404(Ingrediente, pk=id_ingrediente)
    contexto = {'ingrediente': ingrediente}
    return render(request, 'detalleI.html', contexto)

def listaINGREDIENTEConPlantillas(request):
    ingredientes = Ingrediente.objects.order_by('nombre')
    contexto = {'lista_ingredientes': ingredientes}
    return render(request, 'listaI.html', contexto)