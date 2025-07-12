from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250, unique=True)
    body = models.TextField()
    publish = models.DataTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateField(auto_now = True)
    
    class Meta: ordering = ['-publish']
    indexes = [models.Index(fields=['-publish'],)]

    def __str__(self): 
        return self.title