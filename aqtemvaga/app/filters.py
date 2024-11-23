import django_filters
from .models import vaga_oferecido

#Filtros para estado/cidade.
class filtrando_vagas(django_filters.FilterSet):
    class Meta:
        model = vaga_oferecido
        fields = ['Estado', 'Cidade','Bairro','Cargo']
