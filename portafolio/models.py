from django.db import models

# Create your models here.
class Proyecto(models.Model):
    foto = models.ImageField(upload_to="proyectos", null=True)
    titulo = models.CharField (max_length= 100)
    descripcion = models.TextField()
    tags = models.CharField(max_length= 100)
    url_github= models.URLField()

    def __str__(self):
        return self.titulo

