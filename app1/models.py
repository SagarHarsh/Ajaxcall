from django.db import models

# Create your models here.

class DB_save(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    email=models.EmailField()
