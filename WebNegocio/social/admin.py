from django.contrib import admin
from .models import Link

# Register your models here.

class AdminLink(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Empleados').exists():
            return ('key', 'name')
        else: return ('created', 'updated')


admin.site.register(Link, AdminLink)