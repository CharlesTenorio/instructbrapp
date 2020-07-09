from django.contrib import admin
from .models import FeriadoEstadual, FeriadoMunicipal

class FeriadoUfAdmin(admin.ModelAdmin):
    list_display = ('uf', 'nome_feriado', 'data_feriado', 'mes_dia')
    search_fields = ('nome_feriado', )

admin.site.register(FeriadoEstadual, FeriadoUfAdmin)

class FeriadoCidadeAdmin(admin.ModelAdmin):
    list_display = ('cidade', 'nome_feriado', 'data_feriado', 'mes_dia')
    search_fields = ('nome_feriado', )

admin.site.register(FeriadoMunicipal, FeriadoCidadeAdmin)
