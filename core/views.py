from django.shortcuts import render, HttpResponse,redirect
from core.models import Evento

# Create your views here.

# colocando agenda com index
#def index(request):
#    return redirect('/agenda/')

def lista_eventos(request):
    # usuario recebe usuário logado 
    #usuario = request.user
    # evento recebe todos os eventos cadastrados do usuário logado
    #evento = Evento.objects.filter(usuario=usuario)
    # evento recebe todos os eventos cadastrados
    evento = Evento.objects.all()
    #criar lista com eventos recuperados
    dados = {'eventos':evento}
    return render(request,'agenda.html' ,dados)
