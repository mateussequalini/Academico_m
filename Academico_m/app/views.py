from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
class PessoasView(View):
    def get(self, request, *args, **kwargs):
        Pessoas = Pessoa.objects.all()
        return render(request, 'pessoas.html', {'Pessoas':Pessoas})
class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        Ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'Ocupacoes': Ocupacoes})
class  InstituicoesEnsinosView(View):
    def get(self, request, *args, **kwargs):
        InstituicoesEnsinos =  InstituicaoEnsino.objects.all()
        return render(request, ' InstituicaoEnsino.html', {' InstituicoesEnsinos':  InstituicoesEnsinos})
class AreasSaberView(View):
    def get(self, request, *args, **kwargs):
        AreasSaber = AreaSaber.objects.all()
        return render(request, 'AreaSaber.html', {'AreasSaber': AreasSaber})
class CursosView(View):
    def get(self, request, *args, **kwargs):
        Cursos = Curso.objects.all()
        return render(request, 'Curso.html', {'Cursos': Cursos})
class TurmasView(View):
    def get(self, request, *args, **kwargs):
        Turmas = Turma.objects.all()
        return render(request, 'Turma.html', {'Turmas': Turmas})
class DisciplinasView(View):
    def get(self, request, *args, **kwargs):
        Disciplinas = Disciplina.objects.all()
        return render(request, 'Disciplina.html', {'Disciplinas': Disciplinas})
class MatriculasView(View):
    def get(self, request, *args, **kwargs):
        Matriculas = Matricula.objects.all()
        return render(request, 'Matricula.html', {'Matriculas': Matriculas})
class AvaliacoesView(View):
    def get(self, request, *args, **kwargs):
        Avaliacoes = Avaliacao.objects.all()
        return render(request, 'Avaliacao.html', {'Avaliacoes': Avaliacoes})
class FrequenciasView(View):
    def get(self, request, *args, **kwargs):
        Frequencias = Frequencia.objects.all()
        return render(request, 'Frequencia.html', {'Frequencias': Frequencias})
class TurnosView(View):
    def get(self, request, *args, **kwargs):
        Turnos = Turno.objects.all()
        return render(request, 'Turno.html', {'Turnos': Turnos})
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})
class OcorrenciasView(View):
    def get(self, request, *args, **kwargs):
        Ocorrencias = Ocorrencia.objects.all()
        return render(request, 'Occorencia.html', {'Occorencias': Ocorrencias})
class CursoDisciplinasView(View):
    def get(self, request, *args, **kwargs):
        CursoDisciplinas = CursoDisciplina.objects.all()
        return render(request, 'CursoDisciplina.html', {'CursoDisciplinas': CursoDisciplinas})
class AvaliacaoTiposView(View):
    def get(self, request, *args, **kwargs):
        AvaliacaoTipos = AvaliacaoTipo.objects.all()
        return render(request, 'AvaliacaoTipo.html', {'AvaliacaoTipos': AvaliacaoTipos})