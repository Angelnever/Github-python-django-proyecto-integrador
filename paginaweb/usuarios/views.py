from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm
# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')
def single(request):
    return render(request, 'paginas/single.html')
def servicio(request):
    return render(request, 'paginas/servicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def login(request):
    return render(request, 'paginas/login.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    print(usuarios)
    return render(request, 'usuarios/index.html', {'usuarios':usuarios})

def crear(request):
    formulario = UsuarioForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/crear.html', {'formulario': formulario})

def editar(request, id):
    usuario = Usuario.objects.get(id=id)
    formulario = UsuarioForm(request.POST or None, request.FILES or None, instance=usuario)
    if formulario.is_valid() and request.POST :
        formulario.save()
        return redirect('usuarios')
    return render(request, 'usuarios/editar.html', {'formulario': formulario})
def eliminar(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('usuarios')
