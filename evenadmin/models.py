from django.db import models
from django.urls import reverse
from utilisateurs.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
# Create your models here.


class EvenementAdmin(models.Model):
    author    = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to = "even_images", null=True, blank = True)
    slug      = models.SlugField(unique=True, max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    archive   = models.BooleanField(default=False)
    titre     = models.CharField(max_length=255)
    lieu      = models.CharField(max_length=255)
    Date      = models.DateTimeField()
    contenu   = models.TextField()
  

    def __str__(self):
        return f"{self.titre } --- {self.lieu } --- {self.Date}"