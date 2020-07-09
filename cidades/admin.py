from django.contrib import admin
from .models import Cidade, Uf


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('codito_uf', 'codigo_ibge', 'nome')
    search_fields = ('nome', )

admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Uf)
