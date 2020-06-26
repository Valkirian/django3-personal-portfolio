from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image = models.ImageField(
        upload_to='portfolio/media', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, name="Fecha de Creacion")

    # Return el nombre en los elementos creados dentro del admin.
    def __str__(self):
        return self.title
