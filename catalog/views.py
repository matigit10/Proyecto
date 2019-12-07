from django.shortcuts import render, HttpResponse
from .models import TarjetasVideos,Driver,Registro
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

# Create your views here.
def inicio(request):
	Tarjetas= TarjetasVideos.objects.all()
	return render(request,'inicio.html',context={'Tarjetas':Tarjetas,})

def home(request):
	Tarjetas= TarjetasVideos.objects.all()
	return render(request,'home.html',context={'Tarjetas':Tarjetas,})

def link(request):
	Links= TarjetasVideos.objects.all()
	return render(request,'link.html',context={'Links':Links,})

def driverx(request):
	Drivers= Driver.objects.all()
	return render(request,'driverx.html',context={'Drivers':Drivers,})

def ingresar(request):
	registro= Registro.objects.all()
	return render(request,'ingresar.html',context={'registro':registro,})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('registration/login.html')
    template_name = 'signup.html'

class AgregarDriver(CreateView):
	model = Driver
	fields = '__all__'
	initial={'Año':'05/01/2018',}

class DriverUpdate(UpdateView):
	model = Driver
	fields = ['nombre','modelo','año']

class DeleteDriver(DeleteView):
	model = Driver
	success_url = reverse_lazy('delete')