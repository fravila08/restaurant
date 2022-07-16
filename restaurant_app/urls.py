from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('new_ingredient', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredients', views.ingredients, name='ingredients')
]
