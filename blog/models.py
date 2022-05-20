from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    text = models.TextField()
    
    def __str__(self): # добавляет в админке название блога
        return self.title
    
