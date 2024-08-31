from django.shortcuts import render
from .models import Gostos, Cursos, Comidas
# Create your views here.
def index(request):
    contexto = {'Gostos':Gostos.objects.all(), 'Cursos':Cursos.objects.all(), 'Comidas':Comidas.objects.all()}
    return render(request, 'index.html', contexto)

def sobre(request):
    return render(request, 'sobre.html')