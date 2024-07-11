from django.contrib import admin
from .models import Categoria, Licitacion
# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    model = Categoria
    list_display = ('nombre',)

@admin.register(Licitacion)
class LicitacionAdmin(admin.ModelAdmin):
    model = Licitacion
