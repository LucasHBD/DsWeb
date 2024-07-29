from django.contrib import admin
from .models import Pergunta, Alternativa
# Register your models here.

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 2

class PerguntaAdmin(admin.ModelAdmin):
    fieldsets= [
        (None, {'fields':['texto']}),
        ('Informações de data:', {'fields':['data_pub']})
    ]
    inlines = [AlternativaInline]
    list_display = ('texto', 'id', 'data_pub', 'publicada_recentemente')

admin.site.register(Pergunta, PerguntaAdmin)
#admin.site.register(Alternativa, AlternativaInline)