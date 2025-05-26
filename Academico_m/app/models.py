from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área de Saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do saber"
        verbose_name_plural = "Áreas do saber"
class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da instituição de ensino")
    site = models.CharField(max_length=100, verbose_name="Site da instituição de ensino")
    telefone = models.CharField(max_length=100, verbose_name="Telefone da instituição de ensino")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da instituição de ensino")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de ensino"
class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.CharField(max_length=100, verbose_name="Carga Horária Total do curso")
    duracao_meses = models.CharField(max_length=100, verbose_name="Duração (em meses) do curso")
    areasaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área de saber do curso")
    instituicaoensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de ensino do curso")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    pai = models.CharField(max_length=100, verbose_name="Nome do pai da pessoa")
    mae = models.CharField(max_length=100, verbose_name="Nome da mãe da pessoa")
    cpf = models.CharField(max_length=11, verbose_name="CPF da pessoa")
    data_nasc = models.CharField(max_length=100, verbose_name="Data de nascimento da pessoa")
    email = models.CharField(max_length=100, verbose_name="E-mail da pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação da pessoa")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da disciplina")
    areasaber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área de saber da disciplina")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"
class Matricula(models.Model):
    instituicaoensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de ensino da matrícula")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso da matrícula")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa na matrícula")
    data_inicio = models.CharField(max_length=100, verbose_name="Data de início da matrícula")
    data_previsao_termino = models.CharField(max_length=100, verbose_name="Data prevista para o fim da matrícula")

    def __str__(self):
        return f"{self.pessoa} - {self.curso}"

    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "Matrículas"
class Turno(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do turno")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de avaliação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Avaliação Tipo"
        verbose_name_plural = "Avaliações Tipos"
class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da avaliação")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso da avaliação")
    avaliacaotipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo de avaliação")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Frequência no curso")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Frequência na disciplina")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Frequência da pessoa")
    numero_faltas = models.CharField(max_length=100, verbose_name="Número de faltas")

    def __str__(self):
        return f"{self.pessoa} - {self.disciplina} - {self.curso}"

    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da ocorrência")
    data = models.CharField(max_length=100, verbose_name="Data da ocorrência")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso onde ocorreu")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina onde ocorreu")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Pessoa por trás da ocorrência")

    def __str__(self):
        return f"{self.descricao} em {self.data}"

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"
class CursoDisciplina(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplinas do curso")
    cargahoraria = models.CharField(max_length=100, verbose_name="Carga Horária do curso")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso das disciplinas")
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, verbose_name="Turno das disciplinas")

    def __str__(self):
        return f"{self.curso} - {self.disciplina}"

    class Meta:
        verbose_name = "Curso Disciplina"
        verbose_name_plural = "Cursos Disciplinas"