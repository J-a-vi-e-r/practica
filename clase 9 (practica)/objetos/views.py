from django.shortcuts import render
from .models import Objeto

def listar_objetos(request):
    objetos = Objeto.objects.all().order_by('-id')
    return render(request, 'objetos/lista.html', {'objetos': objetos})

def crear_objeto(request):
    if request.method == 'POST':
        formulario = ObjetoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_objetos')
    else:
        formulario = ObjetoForm()
    
    return render(request, 'objetos/formulario.html', {'formulario': formulario, 'titulo': 'Crear Objeto'})

def editar_objeto(request, id):
    objeto = get_object_or_404(Objeto, id=id)
    if request.method == 'POST':
        formulario = ObjetoForm(request.POST, instance=objeto)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_objetos')
    else:
        formulario = ObjetoForm(instance=objeto)
    
    return render(request, 'objetos/formulario.html', {'formulario': formulario, 'titulo': 'Editar Objeto'})

def eliminar_objeto(request, id):
    objeto = get_object_or_404(Objeto, id=id)
    if request.method == 'POST':
        objeto.delete()
        return redirect('listar_objetos')