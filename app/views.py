from django.shortcuts import render, HttpResponse

from app.models import Nota, Posicao, Time


# Create your views here.

def index(request):
    nota = Nota()

    Nota.objects.filter()
    return render(request, 'index.html', {'lista_posicao': Posicao.objects.all(), 'lista_posicao': Posicao.objects.all()})