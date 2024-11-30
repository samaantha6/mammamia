from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from .models import Menu, Plato, Ingrediente
from django.contrib.auth.decorators import permission_required

def index(request):
    return render(request, 'index.html')

@permission_required('myapp.can_view_menu', raise_exception=True)
def listaMenus(request):
    menus = Menu.objects.order_by('nombre')
    return render(request, 'listaM.html', {'lista_menus': menus})

@permission_required('myapp.can_view_menu', raise_exception=True)
def detalleMENU(request, id_menu):
    menu = get_object_or_404(Menu, pk=id_menu)
    platos = menu.platos.all()
    cadenaDeTexto = (f"Menú {menu.nombre}, Descripcion: {menu.descripcion}, Precio: {menu.precio}")
    if platos.exists():
        cadenaDeTexto += "Platos:\n" + "\n".join(f"- {plato.nombre}" for plato in platos)
    else:
        cadenaDeTexto += "No hay platos asociados a este Menú."
    return HttpResponse(cadenaDeTexto)

@permission_required('myapp.can_view_menu', raise_exception=True)
def listaMENUConPlantillas(request):
    menus = Menu.objects.order_by('nombre')
    return render(request, 'listaM.html', {'lista_menus': menus})

@permission_required('myapp.can_view_menu', raise_exception=True)
def detalleMENUConPlantillas(request, id_menu):
    menu = get_object_or_404(Menu, pk=id_menu)
    return render(request, 'detalleM.html', {'menu': menu})

@permission_required('myapp.can_view_plato', raise_exception=True)
def listaPlatos(request):
    platos = Plato.objects.order_by('nombre')
    return render(request, 'listaP.html', {'lista_platos': platos})

@permission_required('myapp.can_view_plato', raise_exception=True)
def detallePLATO(request, id_plato):
    plato = get_object_or_404(Plato, pk=id_plato)
    ingredientes = plato.ingredientes.all()
    cadenaDeTexto = (f"Plato {plato.nombre}, Tipo: {plato.tipo}, Orden: {plato.orden}")
    if ingredientes.exists():
        cadenaDeTexto += "Ingredientes:\n" + "\n".join(f"- {ing.nombre}" for ing in ingredientes)
    else:
        cadenaDeTexto += "No hay ingredientes asociados a este Plato."
    return HttpResponse(cadenaDeTexto)

@permission_required('myapp.can_view_plato', raise_exception=True)
def listaPLATOConPlantillas(request):
    platos = Plato.objects.order_by('nombre')
    return render(request, 'listaP.html', {'lista_platos': platos})

@permission_required('myapp.can_view_plato', raise_exception=True)
def detallePLATOConPlantillas(request, id_plato):
    plato = get_object_or_404(Plato, pk=id_plato)
    return render(request, 'detalleP.html', {'plato': plato})

@permission_required('myapp.can_view_ingrediente', raise_exception=True)
def listaIngredientes(request):
    ingredientes = Ingrediente.objects.order_by('nombre')
    return render(request, 'listaI.html', {'lista_ingredientes': ingredientes})

@permission_required('myapp.can_view_ingrediente', raise_exception=True)
def detalleINGREDIENTE(request, id_ingrediente):
    ingrediente = get_object_or_404(Ingrediente, pk=id_ingrediente)
    return render(request, 'detalleI.html', {'ingrediente': ingrediente})

@permission_required('myapp.can_view_ingrediente', raise_exception=True)
def listaINGREDIENTEConPlantillas(request):
    ingredientes = Ingrediente.objects.order_by('nombre')
    return render(request, 'listaI.html', {'lista_ingredientes': ingredientes})

@permission_required('myapp.can_view_ingrediente', raise_exception=True)
def detalleINGREDIENTEConPlantillas(request, id_ingrediente):
    ingrediente = get_object_or_404(Ingrediente, pk=id_ingrediente)
    return render(request, 'detalleI.html', {'ingrediente': ingrediente})
