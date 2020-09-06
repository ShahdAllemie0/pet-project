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
        form=PetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    context={
        'form':form,
    }
    return render(request,'create.html',context)


def update(request, pet_d):
    pet = Pet.objects.get(id = pet_id)
    form=PetForm(intance = pet)
    if request.method == 'POST':
        form=PetForm(request.POST, request.FILES, intance = pet)
        if form.is_valid():
            form.save()
            return redirect('detail', pet_id)
    context={
        'form':form,
        'pet':pet
    }
    return render(request,'update.html',context)


def delete(request, pet_id):
    pet = Pet.objects.get(id = pet_id)
    pet.delete()
    return redirect('list')
