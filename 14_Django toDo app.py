from django.shortcuts import render
from django.db import models



#class to do male database mast
#added date b database ma ezafe mishe
class Todo(models.Model):
    added_date = models.DateTimeField()
    text = models.CharField(max_length=200)

