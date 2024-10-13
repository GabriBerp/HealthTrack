from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  # O dicionário 'context' passa dados para o template
    context = {
        'message': 'Bem-vindo à minha página no Django!',
    }
    # 'render()' conecta o template HTML com a view
    return render(request, 'home.html', context)
# Create your views here.
