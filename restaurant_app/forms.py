from django.forms import ModelForm
from .models import *

class IngredientForm(ModelForm):
    class Meta:
        model= Ingredient
        fields= ['name', 'quantity', 'price']