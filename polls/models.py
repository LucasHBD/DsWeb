from django.db import models
from django.utils import timezone
import datetime

class Pergunta(models.Model):
    texto = models.CharField(max_length=150)
    data_pub = models.DateTimeField("Data de Publicação: ")

    def __str__(self):
        return self.texto

    def publicada_recentemente(self):
        agora = timezone.now()
        passadas_24h = agora - datetime.timedelta(hours=24)
        return self.data_pub <= agora and self.data_pub >= passadas_24h
    publicada_recentemente.admin_order_field = 'data_pub'
    publicada_recentemente.boolean = True
    publicada_recentemente.short_description = 'É recente?'

class Alternativa(models.Model):
    texto = models.CharField(max_length=100)
    quant_votos = models.IntegerField("Quantidade de Votos: ")
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)

    def __str__(self):
        return "{} ({})".format(self.texto, self.id)