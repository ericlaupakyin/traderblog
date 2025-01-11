from django.contrib import admin
from .models import Category, Content, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id', 'category', 'is_published', 'priority')
   list_display_links = ('id', 'category')
   list_filter = 'category',
   list_editable = 'is_published',
   search_fields = 'category',
   list_per_page = 25
admin.site.register(Category, CategoryAdmin)

class ContentAdmin(admin.ModelAdmin):
   #list_display = ('id', 'category', 'is_published', 'priority')
   list_display=('id','title','body','published_date','is_published','category','priority')
   list_display_links = ('id', 'category')
   list_per_page = 25
admin.site.register(Content, ContentAdmin)

class CommentAdmin(admin.ModelAdmin):
   list_display = ('id','your_name','your_comment','content')
   list_display_links = ('id','your_name')
   list_per_page=25
admin.site.register(Comment,CommentAdmin)
