from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    #еречисляем поля, которые должны отображаться в админке
    list_display = ["text", "pub_date", "author"] 
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ["text"] 
    # добавляем возможность фильтрации по дате
    list_filter = ["pub_date"] 

admin.site.register(Post, PostAdmin)