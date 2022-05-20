from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)
    
    def __str__(self): # добавляет в админке название проекта
        return self.title
    
