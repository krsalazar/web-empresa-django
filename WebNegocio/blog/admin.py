from django.contrib import admin
from .models import Category, Post

# Register your models here.

class AdminCategory(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class AdminPost(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'post_categories','published' ) #Columnas que va a mostrar
    ordering = ('author', 'created') #Ordena los datos
    #Crea una barra de búsqueda
    search_fields = ('title', 'author__username', 'published', 'categories__name') 
    date_hierarchy = 'published'#Filtros de fecha
    list_filter = ('author__username', 'categories__name')

    #Para crear un campo many_to_many en el panel
    def post_categories(self, obj):
        return ", ".join(c.name for c in obj.categories.all().order_by('name'))
    post_categories.short_description = 'Categorías'

admin.site.register(Category, AdminCategory)
admin.site.register(Post, AdminPost)