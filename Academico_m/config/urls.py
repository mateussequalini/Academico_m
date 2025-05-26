from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('pessoas/', PessoasView.as_view(), name='pessoas'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacao'),
    path('instituicaoensino/', InstituicoesEnsinosView.as_view(), name='instituicaoensino'),
    path('areasaber/', AreasSaberView.as_view(), name='areasaber'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('turma/', TurmasView.as_view(), name='turma'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('avaliacao/', AvaliacoesView.as_view(), name='avaliacao'),
    path('frequencia/', FrequenciasView.as_view(), name='frequencia'),
    path('turno/', TurnosView.as_view(), name='turno'),
    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('ocorrencia/', OcorrenciasView.as_view(), name='ocorrencia'),
    path('cursodisciplina/', CursoDisciplinasView.as_view(), name='cursodisciplina'),
    path('avaliacaotipo/', AvaliacaoTiposView.as_view(), name='avaliacaotipo'),
]