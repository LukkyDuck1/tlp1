from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Form_propuesta
from .models import propuesta




@login_required
def base(request):
    user = request.user
    tipo_usuario = None
    if user.groups.filter(name='Estudiante').exists():
        tipo_usuario = 'estudiante'
    elif user.groups.filter(name='Profesor').exists():
        tipo_usuario = 'profesor'
    
    return render(request, 'registration/login.html', {'tipo_usuario': tipo_usuario})

def view_propuesta(request):
    if request.method =='POST':
         print(request.POST)
    form = Form_propuesta(request.POST)
    
    if form.is_valid():
            form.save()
            return redirect('base')
    return render(request, 'registration/login.html',{'form':form})

@login_required
def lista_propuestas(request):
    titulo="carreras"
    propuestas = propuesta.objects.all()

    if 'filtrar_patrocinio' in request.GET:
         propuestas = propuestas.filter(patrocinio=False)
    

    data={
         "titulo":titulo,
         "propuestas":propuestas,

    
    }

    return render(request, 'registration/login.html',data)


@login_required
def editar_propuesta(request, id):
    propuesta_instance = get_object_or_404(propuesta, id=id)
    
    form = Form_propuesta(request.POST, instance=propuesta_instance)
    if form.is_valid():
        form.save()
        return redirect('lista')
    else:
        form = Form_propuesta(instance=propuesta_instance)
    
    return render(request, 'registration/login.html', {'form': form})



def lista_propuestas_anon(request):
    titulo="carreras"
    propuestas = propuesta.objects.all()

    propuestas = propuestas.filter(patrocinio=True)
    

    data={
         "titulo":titulo,
         "propuestas":propuestas,

    
    }

    return render(request, 'registration/login.html',data)