from rest_framework import serializers # type: ignore
from .models import vaga_oferecido

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = vaga_oferecido
        fields = ['id', 'Região', 'Cidade', 'Cargo', 'Salário', 'Requisitos', 'Benifícios', 'Descrição', 'Empresa', 'Contato']
