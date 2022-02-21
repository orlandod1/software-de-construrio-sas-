from django.contrib import admin

from apps.material.models import Material

# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
     search_fields= ('ma_nombre'),
     ordering = ['ma_nombre']
admin.site.register(Material,MaterialAdmin)