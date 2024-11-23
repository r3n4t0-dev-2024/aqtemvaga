from django import forms
from .models import*

class VagaForm(forms.ModelForm):
    class Meta:
        model = vaga_oferecido
        fields = ['Estado', 'Cidade','Bairro', 'Cargo', 'Salário', 'Requisitos', 'Benifícios', 'Descrição', 'Empresa', 'Contato']
        widgets = {
            'Estado': forms.Select(attrs={'class': 'form-control'}),
            'Cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'Bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'Cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'Salário': forms.TextInput(attrs={'class': 'form-control'}),
            'Requisitos': forms.Textarea(attrs={'class': 'form-control'}),
            'Benifícios': forms.Textarea(attrs={'class': 'form-control'}),
            'Descrição': forms.Textarea(attrs={'class': 'form-control'}),
            'Empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'Contato': forms.TextInput(attrs={'class': 'form-control'}),
        }
       

class CurriculoForm(forms.ModelForm):
    class Meta:
        model = Curriculo
        fields = ['cargo_pretendido','salário_pretendido','arquivo']
        widgets = { 
            'salário_pretendido': forms.TextInput(attrs={'placeholder': '0.000,00'}),
        }
        
        

class PerfilCandidatoForm(forms.ModelForm):
    class Meta:
        model = PerfilCandidato
        fields = ['nome_completo', 'telefone', 'endereco', 'cidade', 'bairro', 'perfil_profissional', 'experiencia_profissional', 'formacao_academica', 'cursos']



class VisualizacaoForm(forms.ModelForm):
    class Meta:
        model = view_perfil_candidato
        fields = ['visualizador_curriculo']