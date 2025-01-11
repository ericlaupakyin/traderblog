from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='articles'),
    path('article', views.article, name='article'),
]
