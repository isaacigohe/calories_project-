from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from django.db.models import Sum

def index(request):
    """
    View to display all food items and handle adding new items.
    """
    if request.method == "POST":
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories:
            Food.objects.create(name=name, calories=calories)
        return redirect('index')

    food_items = Food.objects.all().order_by('-created_at')
    total_calories = food_items.aggregate(Sum('calories'))['calories__sum'] or 0
    
    context = {
        'food_items': food_items,
        'total_calories': total_calories,
    }
    return render(request, 'calorie_tracker/index.html', context)

def delete_food(request, pk):
    """
    View to remove a food item from the list.
    """
    food = get_object_or_404(Food, id=pk)
    food.delete()
    return redirect('index')

def reset_calories(request):
    """
    View to clear all food items and reset the calorie count.
    """
    Food.objects.all().delete()
    return redirect('index')
