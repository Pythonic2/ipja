from django.shortcuts import render, redirect
from django.conf import settings
import logging
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .forms import AvaliacaoForm
from .models import Avaliacao
logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = '1.html'
    form_class = AvaliacaoForm
    
    def get(self, request):
        context = {'form': self.form_class}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            print('aqyu')
            form.save()
            return redirect('home')  # Remover a vírgula aqui
        else:
            
            context = {'form': form,'erros':form.errors}
            return render(request, self.template_name, context)

    
class ListAvaliacoesView(TemplateView):
    template_name = 'itens-fornecedores.html'
   
    
    def get(self, request):
      
        avaliacoes = Avaliacao.objects.all().order_by('-id')
        context = {'avaliacoes':avaliacoes}
        return render(request, self.template_name, context)
    