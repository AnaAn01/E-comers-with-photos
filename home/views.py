from django.shortcuts import render
from home.models import Item


def home_index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'home_index.html', context)