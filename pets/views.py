from django.shortcuts import render.redirect
from .models import Pet

# Create your views here.
def list(request):
    pets = Pet.objects.filter(available=True)
    context = {
    "pets": pets,
    }
    return render(request, 'list.html', context)
