from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# criando tabela Evento
class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(blank=True, null=True,verbose_name="Descrição")
    data_evento = models.DateTimeField(verbose_name="Data do Evento")
    data_criacao = models.DateTimeField(auto_now=True,verbose_name="Data da Criação")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Usuário")

    #definindo nome da tabela
    class Meta:
        db_table = 'evento'
    
    # listagem conterá o titulo como link pro registro
    def __str__(self):
        return self.titulo
    
    # formata data
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M H')