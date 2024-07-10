from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = 'Todo'
        # verbose_name_plural = 'Todos'    