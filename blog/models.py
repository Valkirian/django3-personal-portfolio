from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to="blog/media", blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    date = models.DateField()

    # Return el nombre en los elementos creados dentro del admin.
    def __str__(self):
        return self.title
