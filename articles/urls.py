from django.urls import path, include
from . import views

# urlpatterns = [
#     path('', views.index, name='articles'),
#     path('article', views.article, name='article'),
# ]

urlpatterns = [
    path('', views.index, name='articles'),
    path('article', views.article, name='article'),
    path('articles/<int:category_id>', views.articles, name='articles'),
    path('article/<int:content_id>', views.article, name='article'),
    path('comments/<int:content_id>', views.comments, name='comments'),        
]