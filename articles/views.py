from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Content

def index(request):
    contents = Content.objects.order_by('-published_date').filter(category_id=2)
    # 分頁
    paginator = Paginator(contents,4)
    page_number = request.GET.get('page')
    paged_contents = paginator.get_page(page_number)

    context = {
        'contents' : paged_contents,
    }
    return render(request, 'articles/articles.html', context)

def article(request):
    return render(request,'articles/article.html')