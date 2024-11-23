from django.contrib import admin
from .models import*


# Regiter/Empregador.
@admin.register(vaga_oferecido)

class Admin(admin.ModelAdmin):
  list_display = ('Estado', 'Cidade','Bairro', 'Cargo', 'Salário', 'Requisitos', 'Benifícios', 'Descrição', 'Empresa', 'Contato')


# Regiter/Atemvaga_brasil/BlogPost
admin.site.register(aqtemvaga_brasil)
admin.site.register(BlogPost)
admin.site.register(PerfilCandidato)
admin.site.register(Empregador)
admin.site.register(Curriculo)
    
    
# Regiter/Atemvaga_região.
@admin.register(aqtemvaga_regiao)
class Admin(admin.ModelAdmin):
  list_display = ('Regiao','Cidade','Salario','Requisitos','Benificios','Descrição','Empresa','Contato')
    
    
# Regiter/Curitiba_região.   
@admin.register(curitiba_regiao)
class Admin(admin.ModelAdmin):
  list_display = ('Regiao','Cidade','Salario','Requisitos','Benificios','Descrição','Empresa','Contato')
    
    
# Regiter/Maringa_regiao.
@admin.register(maringa_regiao)
class Admin(admin.ModelAdmin):
  list_display = ('Regiao','Cidade','Salario','Requisitos','Benificios','Descrição','Empresa','Contato')
        
