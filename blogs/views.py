from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Category
from articles.models import Content

# Create your views here.

def index(request):
    categorys = Category.objects.order_by('-priority').filter(is_published=True)
    contents = Content.objects.all()
    context = {
        'categorys' : categorys,
        'contents' : contents
    }
    return render(request, 'blogs/index.html', context)

def about(request):
    return render(request,'blogs/about.html')

def service(request):
    return render(request,'blogs/service.html')