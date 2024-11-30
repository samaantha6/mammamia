from django.contrib import admin
from .models import Menu, Plato, Ingrediente

class MenuAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('myapp.can_view_menu')

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('myapp.can_edit_menu')

admin.site.register(Menu, MenuAdmin)

class PlatoAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('myapp.can_view_plato')

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('myapp.can_edit_plato')

admin.site.register(Plato, PlatoAdmin)

class IngredienteAdmin(admin.ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return request.user.has_perm('myapp.can_view_ingrediente')

    def has_change_permission(self, request, obj=None):
        return request.user.has_perm('myapp.can_edit_ingrediente')

admin.site.register(Ingrediente, IngredienteAdmin)
