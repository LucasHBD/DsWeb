from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pergunta_id>/detalhes', views.detalhes, name='detalhes'),
    path('<int:pergunta_id>/votacao', views.votacao, name='votacao'),
    path('<int:pergunta_id>/resultado', views.resultado, name='resultado'),
]