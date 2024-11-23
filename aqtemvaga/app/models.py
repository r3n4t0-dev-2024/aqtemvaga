from django.db import models
import datetime
from django.urls import reverse
import pytz
from django.utils.timezone import now
from django.contrib.auth.models import User

# Modelo Aqtemvaga_Brasil.
class aqtemvaga_brasil(models.Model):
  Estado = models.CharField(max_length=20,null=True) 
  def __str__(self) -> str: return f"{self.Estado}"
 
 
# Modelo Aqtemvaga_Região. 
class aqtemvaga_regiao(models.Model):
  Regiao = models.ForeignKey(aqtemvaga_brasil, on_delete=models.CASCADE)
  Cidade = models.CharField(max_length=100)
  bairro = models.CharField(max_length=100,null=True) 
  Cargo = models.CharField(max_length=100)
  Salario = models.CharField(max_length=100)
  Requisitos = models.TextField()
  Benificios = models.TextField()
  Descrição = models.TextField()
  Empresa = models.TextField()
  Contato = models.TextField()
  Codigo = models.CharField(max_length=150)
  Data_criacao = models.DateTimeField(default=now)
  Data_atualizacao = models.DateTimeField(auto_now=True)
  
  
#NÃO PRECISA USAR NO MODELO.PY 
class curitiba_regiao(models.Model):
  Regiao = models.ForeignKey(aqtemvaga_brasil, on_delete = models.CASCADE)
  Cidade = models.CharField(max_length=100)
  Cargo = models.CharField(max_length=100)
  Salario = models.CharField(max_length=100)
  Requisitos = models.TextField()
  Benificios= models.TextField()
  Descrição = models.TextField()
  Empresa = models.TextField()
  Contato = models.TextField()
  Codigo = models.CharField(max_length=150)
  Data_criacao = models.DateTimeField(default=now)
  Data_atualizacao = models.DateTimeField(auto_now=True)
  
  
# Modelo Blog do site AQ!temvagas. 
class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    url = models.URLField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo


#NÃO PRECISA USAR NO MODELO.PY 
class maringa_regiao(models.Model):
  Regiao = models.ForeignKey(aqtemvaga_brasil, on_delete = models.CASCADE)
  Cidade = models.CharField(max_length=100)
  Cargo = models.CharField(max_length=100)
  Salario = models.CharField(max_length=100)
  Requisitos = models.TextField()
  Benificios= models.TextField()
  Descrição = models.TextField()
  Empresa = models.TextField()
  Contato = models.TextField()
  Codigo = models.CharField(max_length=150)
  Data_criacao = models.DateTimeField(default=now)
  Data_atualizacao = models.DateTimeField(auto_now=True)
  
  
# Modelo para empregadores cadastras vagas.
class Empregador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    primeiro_nome = models.CharField(max_length=30, null=True) # Adicionando o campo para o primeiro nome
    nome_da_empresa = models.CharField(max_length=255,null=True)
    descricao_da_empresa = models.TextField(blank=True, null=True)  # Tornar opcional
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    def __str__(self): return f'{self.nome_da_empresa}'
    
    
class vaga_oferecido(models.Model):
    Empregador = models.ForeignKey(Empregador, on_delete=models.CASCADE)
    Estado = models.ForeignKey(aqtemvaga_brasil, on_delete=models.CASCADE, null=True)
    Cidade = models.CharField(max_length=100, blank=True, null=True)
    Bairro = models.CharField(max_length=100,blank=True, null=True) 
    Cargo = models.CharField(max_length=100, blank=True, null=True)  # Tornar opcional
    Salário = models.CharField(max_length=100, blank=True, null=True)  # Tornar opcional
    Requisitos = models.TextField(blank=True, null=True)  # Tornar opcional
    Benifícios = models.TextField(blank=True, null=True)  # Tornar opcional
    Descrição = models.TextField(blank=True, null=True)  # Tornar opcional
    Empresa = models.TextField(blank=True, null=True)  # Tornar opcional
    Contato = models.TextField(blank=True, null=True)  # Tornar opcional
    Data_criacao = models.DateTimeField(default=now)
    Data_atualizacao = models.DateTimeField(auto_now=True)
    
# Anexar Currículo/Candidato 
class Curriculo(models.Model):
    empregador = models.ForeignKey(Empregador, on_delete=models.CASCADE,null=True, related_name='curriculos')
    salário_pretendido = models.CharField(max_length=100, null=True, blank=True)
    cargo_pretendido = models.CharField(max_length=100, null=True, blank=True) # Novo campo para Cargo
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,null=True) # Alterado para PROTECT
    arquivo = models.FileField(upload_to='curriculos/')
    data_envio = models.DateTimeField(auto_now_add=True)
    deletado_pelo_empregador = models.BooleanField(default=False)
    deletado_pelo_candidato = models.BooleanField(default=False)
    def __str__(self): return f'{self.usuario.username} - {self.cargo_pretendido} {self.salário_pretendido}'
    
    
# Atualização de Cadastro/Candidato
class PerfilCandidato(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    perfil_profissional = models.TextField()
    experiencia_profissional = models.TextField()
    formacao_academica = models.TextField()
    cursos = models.TextField()

    def __str__(self):
        return self.usuario.username


#NÃO PRECISA USAR NO MODELO.PY
class VisualizacaoCurriculo(models.Model):
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)
    visualizador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visualizador')
    data_visualizacao = models.DateTimeField(auto_now_add=True)
    visualizacoes_count = models.PositiveIntegerField(default=0)
    def __str__(self): return f'{self.visualizador.username} visualizou o currículo de {self.curriculo.usuario.username}'
    

#NÃO PRECISA USAR NO MODELO.PY
class view_perfil_candidato(models.Model):
    curriculo_candidato = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='curriculos_candidato')
    curriculo_visualizar = models.ForeignKey(Curriculo, on_delete=models.CASCADE)
    visualizador_curriculo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='curriculos_visualizados')
    data_vews = models.DateTimeField(auto_now_add=True)


# Envio de curriculo/candidato
class EnvioCurriculo(models.Model):
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)
    vaga = models.ForeignKey(vaga_oferecido, on_delete=models.CASCADE)
    data_envio = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('curriculo', 'vaga')
    
    def __str__(self):
        return f'Currículo de {self.curriculo.usuario.username} enviado para a vaga {self.vaga.Cargo}'

  
