from django.shortcuts import render, redirect
from django.conf import settings
import logging
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .forms import AvaliacaoForm
from .models import Avaliacao, PrevDizimos
from django.utils.translation import gettext_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime


logger = logging.getLogger(__name__)

class LoginUsuario(LoginView):
    template_name = 'login.html'
    def form_invalid(self, form):
        username = form.cleaned_data.get('username')
        print(username)
        user_exists = User.objects.filter(username=username).exists()

        error_messages = {
            'invalid_login': gettext_lazy('Verifique o usuário e senha e tente novamente.'),
            'inactive': gettext_lazy('Usuário inativo.'),
        }
        print(error_messages['invalid_login'])
        AuthenticationForm.error_messages = error_messages
        return super().form_invalid(form)
    

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


def calcular_dizimos_por_ano():
    # Obter todos os anos disponíveis nas avaliações
    anos_disponiveis = Avaliacao.objects.dates('data_avaliacao', 'year')

    for ano in anos_disponiveis:
        # Filtrar as Avaliações pelo ano específico
        avaliacoes_do_ano = Avaliacao.objects.filter(data_avaliacao__year=ano.year)

        # Calcular a soma dos dízimos para o ano
        total_dizimos = avaliacoes_do_ano.aggregate(Sum('dizimo'))['dizimo__sum'] or 0

        # Verificar se já existe um registro para o ano no modelo PrevDizimos
        prev_dizimos, created = PrevDizimos.objects.get_or_create(ano=ano.year, defaults={'valor': total_dizimos})

        # Se já existe, atualiza o valor
        if not created:
            prev_dizimos.valor = total_dizimos
            prev_dizimos.save()

    return "Cálculo e salvamento de dízimos concluído."
    

class ListAvaliacoesView(TemplateView):
    template_name = 'itens-fornecedores.html'
   
    @method_decorator(login_required)
    def get(self, request):
        
        avaliacoes = Avaliacao.objects.all().order_by('-id')
        mensagem = calcular_dizimos_por_ano()
        ano_atual = datetime.now().year

        # Obter todas as avaliações
        avaliacoes = Avaliacao.objects.all().order_by('-id')
        
        # Calcular dízimos (se necessário, ajuste essa função conforme sua lógica)
        mensagem = calcular_dizimos_por_ano()

        # Filtrar dízimos pelo ano atual
        prev_diz = PrevDizimos.objects.filter(ano=ano_atual)

        # Criar contexto
        context = {
            'avaliacoes': avaliacoes,
            'dizimos': [dizimo.valor for dizimo in prev_diz]
        }
        return render(request, self.template_name, context)
    

def detalhe_avaliacao_htmx(request,va_id):
    print("aqui")
    av = Avaliacao.objects.get(id=va_id)
    print(av.nome)
    return render(request,'parciais/detalhe_avaliacao.html',{'avaliacao':av})