from django.db import models

class Teacher(models.Model):
    name=models.CharField(max_length=100)
    subject=models.CharField(max_length=200)
    contact=models.CharField(max_length=15)
    email=models.EmailField(unique=True)
   
    
    
    def __str__(self):
        return (f"{self.name}-{self.subject}")