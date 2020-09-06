from django.shortcuts import render, redirect
from .models import Pet
from .forms import PetForm

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

def create(request):
    form=PetForm()
    if request.method == 'POST':
        form=PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context={
        'form':form,
    }
    return render(request,'create.html',context)
