from email.errors import MalformedHeaderDefect
from tkinter import CASCADE
from django.db import models
from django.forms import CharField, FloatField

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=250)
    
class Ingredient(models.Model):
    name=models.CharField(max_length=250)
    quantity=models.FloatField(default=0)
    price=models.FloatField(default=0.25)
    
    def get_absolute_url(self):
        return 'ingredients'
    
    def __str__(self):
        return f'{self.name} and cost {self.price}'
    
    
class RecipeRequirements(models.Model):
    name=models.CharField(max_length=250)
    ingredients=models.CharField(max_length=250)
    
    
class MenuItem(models.Model):
    name=models.CharField(max_length=250)
    recipe=models.ForeignKey('RecipeRequirements', on_delete=models.CASCADE)
    price=models.FloatField()
    
class PurchaseHistory(models.Model):
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE)
    item=models.ForeignKey("MenuItem", on_delete=models.CASCADE)

