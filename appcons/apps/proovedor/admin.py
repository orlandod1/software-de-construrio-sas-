from django.contrib import admin

from apps.proovedor.models import Proovedor 

# Register your models here.
class ProovedorAdmin(admin.ModelAdmin):

     search_fields= ('proov_nombre'),
admin.site.register(Proovedor,ProovedorAdmin)
