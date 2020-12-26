from django.contrib import admin
from .models import Classe
# Register your models here.


def publish(ModelAdmin, request, queryset):
    queryset.update(posted=True)


def unpublish(ModelAdmin, request, queryset):
    queryset.update(posted=False)


publish.short_description = "Post selected classes"
unpublish.short_description = "Remove selected classes from site"


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    actions = [publish, unpublish]
    search_fields = ['name', 'classe_groupe', 'prof', 'start', 'end']
    list_display = ('name', 'classe_groupe', 'prof', 'start', 'code', 'posted')
    list_filter = ('classe_groupe', 'prof', 'posted')
