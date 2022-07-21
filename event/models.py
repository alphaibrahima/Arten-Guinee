from django.db import models
from django.urls import reverse
from utilisateurs.models import User
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify



class Event(models.Model):
    thumbnail     = models.ImageField(upload_to = "even_images", null=True, blank = True)
    author        = models.ForeignKey(User, on_delete=models.CASCADE)
    slug          = models.SlugField(unique=True, max_length=100)
    timestamp     = models.DateTimeField(auto_now_add=True)
    titre         = models.CharField(max_length=255)
    lieu          = models.CharField(max_length=255)
    views         = models.IntegerField(default=1)
    Date          = models.DateTimeField()
    tags          = TaggableManager() 
    description   = models.TextField()

    def __str__(self):
        return f"{self.titre } --- {self.lieu } --- {self.Date}"


    def save(self, *args, **kwargs):
        self.slug = slugify(self.titre)
        super(Event, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("evens")

    
