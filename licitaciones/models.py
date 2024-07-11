from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.nombre

class Licitacion(models.Model):
    titulo = models.CharField(max_length=30)
    categorias = models.ManyToManyField(Categoria)
    precio_total = models.IntegerField()

    class Meta:
        verbose_name = 'licitacion'
        verbose_name_plural = 'licitaciones'
    def __str__(self):
        return self.titulo
