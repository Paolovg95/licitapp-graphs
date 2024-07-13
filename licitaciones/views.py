from django.shortcuts import render
from .models import Categoria, Licitacion
from collections import Counter

# Create your views here.


def panel(request):
    licitaciones = Licitacion.objects.all()
    categorias = Counter()

    for licitacion in licitaciones:
        for categoria in licitacion.categorias.all():
            categorias[categoria.nombre] += 1

    gastos_per_categoria = {}

    for categoria in categorias.keys():
        gastos_per_categoria[categoria] = 0
        for licitacion in licitaciones.filter(categorias__nombre=categoria):
            gastos_per_categoria[categoria] += licitacion.precio_total

    data = {"categorias": categorias, "gastos_per_categoria": gastos_per_categoria}

    return render(request, "panel.html", data)
