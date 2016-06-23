from django.contrib import admin
from django.contrib.admin import site, ModelAdmin
from models import Post, Project

def categories(instance):
    return ', '.join(instance.categories)

class PostAdmin(ModelAdmin):
    list_display = ['title', categories]



class Post(admin.ModelAdmin):
    model = Post


admin.site.register(Project)
admin.site.register(Post)
admin.site.register(Project)
admin.site.register(PostAdmin)
site.register(Post, PostAdmin)