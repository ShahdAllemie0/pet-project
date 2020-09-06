from django.shortcuts import render, redirect
from .models import Pet

# Create your views here.
def list(request):
    pet = Pet.objects.filter(available=True)
    context = {
    "pet": pet,
    }
    return render(request, 'list.html', context)


def detail(request, pet_id):
    pet = Pet.objects.get(id = pet_id)

    context = {

    "pet": pet,

    }
    return render(request, 'detail.html', context)
