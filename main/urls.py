from django.urls import path
from .views import IndexView,ListAvaliacoesView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('avaliacoes/', ListAvaliacoesView.as_view(), name='avaliacoes'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
