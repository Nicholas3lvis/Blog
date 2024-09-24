from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Blog, Comment
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=['author','title','body','created','slug','img']
    prepopulated_fields={'slug':('title',)}
    
    
class ComentAdmin(admin.ModelAdmin):
    list_display=['user','body','created']
    # summernote_fields = ('body', ) 
    
admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Comment, ComentAdmin)



# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content', )


# admin.site.register(Post, PostAdmin)