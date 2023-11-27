from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Persona


# Create your views here.
def home(request):
    nro_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    #personas = Persona.objects.order_by('-id')
    personas = Persona.objects.order_by('nombre','id')
    return render(request,'home.html', {'nro_personas':nro_personas,'personas':personas})
