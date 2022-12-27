from django.shortcuts import render
from home.models import Item


def home_index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'home_index.html', context)


def home_detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item
    }
    return render(request, 'home_detail.html', context)