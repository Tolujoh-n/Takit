from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Create your views here.
def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)



