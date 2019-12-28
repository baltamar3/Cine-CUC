from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import Funcion, Solicitud, Pelicula
from .forms import FuncionForm

# Create your views here.


class FuncionListView(ListView):
    model = Funcion

def FuncionDetailView(request, pk):
    funcion = Funcion.objects.get(pk=pk)
    solicitudes= Solicitud.objects.filter(funcion=funcion)
    return render(request, 'cine/funcion_detail.html', {"funcion":funcion, "solicitudes":solicitudes})


class FuncionCreate(CreateView):
    model = Funcion
    form_class = FuncionForm
    success_url = reverse_lazy('listar-funciones')

class PeliculaCreate(CreateView):
    model = Pelicula
    fields = ['nombre', 'descripcion','director', 'genero']
    success_url = reverse_lazy('listar-funciones')    

class FuncionUpdate(UpdateView):
    model = Funcion
    fields = ['pelicula', 'fecha_inicio',
              'fecha_fin', 'lugar', 'direccion', 'cupos']
    success_url = reverse_lazy('listar-funciones')


def FuncionDelete(request, pk):
    funcion = Funcion.objects.get(pk=pk)
    funcion.estado="Cancelada"
    funcion.save()
    return redirect('listar-funciones')


@csrf_exempt
@login_required(login_url='login')
def SolicitarCupo(request, id):
    if request.method == "POST":
        num_cupos = int(request.POST["numCupos"])
        funcion = get_object_or_404(Funcion, pk=id)
        if num_cupos <= funcion.cupos and num_cupos >= 0:
            solicitud = Solicitud.objects.create(usuario=request.user, funcion= funcion, num_boletas=num_cupos)
            solicitud.save()
            funcion.evaluar(num_cupos)
    return redirect('listar-funciones')
