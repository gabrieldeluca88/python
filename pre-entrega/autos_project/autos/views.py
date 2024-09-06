from django.shortcuts import render, redirect
from .models import Cliente, Modelo, Auto
from .forms import ClienteForm, ModeloForm, AutoForm, BuscarForm
from django.db.models import Q

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_cliente')
    else:
        form = ClienteForm()
    return render(request, 'agregar_cliente.html', {'form': form})

def agregar_modelo(request):
    if request.method == 'POST':
        form = ModeloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_modelo')
    else:
        form = ModeloForm()
    return render(request, 'agregar_modelo.html', {'form': form})

def agregar_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_auto')
    else:
        form = AutoForm()
    return render(request, 'agregar_auto.html', {'form': form})

def buscar(request):
    form = BuscarForm()
    results = []
    if 'query' in request.GET:
        query = request.GET['query']
        
        # Busca en modelos
        autos_por_modelo = Auto.objects.filter(modelo__nombre__icontains=query)
        
        # Busca en clientes (nombre y país de origen)
        autos_por_cliente = Auto.objects.filter(
            Q(cliente__nombre__icontains=query) |
            Q(cliente__pais_origen__icontains=query)
        )
        
        # Combina los resultados de ambas búsquedas
        results = autos_por_modelo | autos_por_cliente
        
    return render(request, 'buscar.html', {'form': form, 'results': results})

def inicio(request):
    return render(request, 'inicio.html')
