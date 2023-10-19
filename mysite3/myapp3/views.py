from .forms import CreateContactForm, UpdateContactForm
from .models import Contactlist
from django.http import HttpResponseRedirect
from django.shortcuts import render

def home(request):
 if request.method == 'POST':
  form = CreateContactForm(request.POST)
  if form.is_valid():
   formdata = form.cleaned_data
   id = formdata['id']
   name = formdata['name']
   address = formdata['address']
   profession = formdata['profession']
   profession2 = formdata['profession2']
   number = formdata['number']
   email = formdata['email']
   if profession == profession2:
    return HttpResponseRedirect('/error')
   Contactlist.objects.create(id=id, name=name, address=address, profession=profession, profession2=profession2, number=number, email=email)
   return HttpResponseRedirect('/success')
 else:
  form = CreateContactForm()
 list = Contactlist.objects.all()
 return render(request, 'myapp3/index.html', {'form': form, 'list': list})

def success(request):
 return render(request, 'myapp3/success.html')

def error(request):
 return render(request, 'myapp3/error.html')

def view(request, id):
 object = Contactlist.objects.get(id=id)
 return render(request, 'myapp3/view.html', {'object': object})

def edit(request, id):
 object = Contactlist.objects.get(id=id)
 if request.method == 'POST':
  form = UpdateContactForm(request.POST)
  if form.is_valid():
    formdata = form.cleaned_data
    object.name = formdata['name']
    object.address = formdata['address']
    object.profession = formdata['profession']
    object.profession2 = formdata['profession2']
    object.number = formdata['number']
    object.email = formdata['email']
    object.save()
    return HttpResponseRedirect('/success')
 else:
  form = UpdateContactForm()
 return render(request, 'myapp3/edit.html', {'object': object, 'form': form})

def delete(request,id):
 object = Contactlist.objects.get(id=id)
 object.delete()
 return HttpResponseRedirect('/success')
