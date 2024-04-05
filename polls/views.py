from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Pergunta, Alternativa

# Create your views here.
def index(request):
    lista = Pergunta.objects.all()
    template = loader.get_template('polls/index.html')
    contexto = {'lista_enquetes': lista}
    return HttpResponse(template.render(contexto, request))

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = {'enquete': pergunta}
    return render(request, 'polls/detalhes.html', contexto)

def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        id_alternativa = request.POST['escolha']
        alt = pergunta.alternativa_set.get(pk=id_alternativa)
    except (KeyError, Alternativa.DoesNotExist):
        contexto = {
            'enquete': pergunta,
            'error': 'Você precisa selecionar uma alternativa.'
        }
        return render(request, 'polls/detalhes.html', contexto)
    else:
        alt.quant_votos += 1
        alt.save()
        return HttpResponseRedirect(reverse('polls:resultado', args=(pergunta.id,)
        ))

def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk = pergunta_id)
    contexto = {'enquete': pergunta}
    return render(request, 'polls/resultado.html', contexto)