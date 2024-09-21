from django.urls import path
from .views import IndexView,ListAvaliacoesView, LoginUsuario, detalhe_avaliacao_htmx, sucesso,detalhe_avaliacao_mobile
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

# Definindo o handler da página 404
handler404 = 'django.views.defaults.page_not_found'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('avaliacoes/', ListAvaliacoesView.as_view(), name='avaliacoes'),
    path('login/', LoginUsuario.as_view(), name='login'),
    path('sucesso/',sucesso, name='sucesso'),
    path('detalhe-avaliacao/<int:va_id>/', detalhe_avaliacao_htmx, name='detalhe-avaliacao'),
    path('detalhe-avaliacao-mobile/<int:va_id>/', detalhe_avaliacao_mobile, name='detalhe-avaliacao-mobile'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
