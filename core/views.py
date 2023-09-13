from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from core.models import Evento
from django.contrib import messages


# Create your views here.

# colocando agenda com index
#def index(request):
#    return redirect('/agenda/')
def login_user(request):
   return render(request, 'login.html')

def logout_user(request):
    #limpando a sessão
    logout(request)
    return redirect ('/')

def submit_login(request):
    if request.POST:
        username= request.POST.get('username')
        password=request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            #gerando amensagem de erro no Login
            messages.error(request,"Usuário ou senha inválida!")
    return redirect('/')

#verificar se está logado
@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    # usuario recebe usuário logado 
    #usuario = request.user
    # evento recebe todos os eventos cadastrados do usuário logado
    #evento = Evento.objects.filter(usuario=usuario)
    # evento recebe todos os eventos cadastrados
    evento = Evento.objects.filter(usuario=usuario)
    #criar lista com eventos recuperados
    dados = {'eventos':evento}
    return render(request,'agenda.html' ,dados)
