from django.urls import path
from .views import FuncionListView, FuncionDelete, FuncionUpdate, FuncionCreate, SolicitarCupo, FuncionDetailView, PeliculaCreate

urlpatterns = [
    path('',FuncionListView.as_view(), name="listar-funciones"),
    path('funcion/crear/',FuncionCreate.as_view(), name="crear-funcion"),
    path('funcion/detalles/<int:pk>', FuncionDetailView, name='detalles-funcion'),
    path('funcion/borrar/<int:pk>', FuncionDelete, name='elminar-funcion'),
    path('funcion/editar/<int:pk>', FuncionUpdate.as_view(), name='editar-funcion'),
    path('funcion/solicitar/<int:id>', SolicitarCupo, name='solicitar-funcion'),
    path('pelicula/crear/',PeliculaCreate.as_view(), name="crear-pelicula"),
]