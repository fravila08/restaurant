from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'restaurant_app/home.html')

class IngredientCreate(CreateView):
    model = Ingredient
    template_name= 'restaurant_app/new_ingredient.html'
    form_class= IngredientForm
    
def ingredients(request):
    product=Ingredient.objects.all()
    context={
        'product':product    
    }
    return render(request, 'restaurant_app/ingredients.html', context)
    