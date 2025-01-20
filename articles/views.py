from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Category, Content, Comment

# def index(request):
#     contents = Content.objects.order_by('-published_date').filter(category_id=2)
#     # 分頁
#     paginator = Paginator(contents,4)
#     page_number = request.GET.get('page')
#     paged_contents = paginator.get_page(page_number)

#     context = {
#         'contents' : paged_contents,
#     }
#     return render(request, 'articles/articles.html', context)

# def article(request):
#     return render(request,'articles/article.html')

def index(request):

    categorys = Category.objects.order_by('-priority').filter(is_published=True)
    contents = Content.objects.all()

    paginator = Paginator(contents,4)
    page_number = request.GET.get('page')
    paged_contents = paginator.get_page(page_number)

    context = {
        'categorys' : categorys,
        'contents' : paged_contents,
    }
    return render(request, 'articles/articles.html', context)

def articles(request, category_id):

    categorys = Category.objects.order_by('-priority').filter(is_published=True)
    contents = Content.objects.order_by('-published_date').filter(is_published=True).filter(category_id=category_id)

    paginator = Paginator(contents,4)
    page_number = request.GET.get('page')
    paged_contents = paginator.get_page(page_number)

    context = {
        'categorys' : categorys,
        'contents' : paged_contents,
    }

    return render(request, 'articles/articles.html', context)


def article(request, content_id):

    categorys = Category.objects.order_by('-priority').filter(is_published=True)
    content = get_object_or_404(Content, pk=content_id)

    content = get_object_or_404(Content, pk=content_id)


    if request.method == 'POST':
        your_name = request.POST['your_name']
        your_comment = request.POST['your_comment']
        print(your_name)
        print(your_comment)

        if Comment.objects.filter(your_name=your_name).filter(your_comment=your_comment).exists():
            print('comment already taken')
            
        else:
            comment = Comment(content_id=content_id, your_name=your_name, your_comment=your_comment)
            comment.save()
            print('comment saved.')


    context = {
        'categorys' : categorys,
        "content" : content,
        }

    return render(request,'articles/article.html', context)



def comments(request, content_id):

    categorys = Category.objects.order_by('-priority').filter(is_published=True)
    content = Content.objects.get(id=content_id)
    comments = Comment.objects.filter(content_id=content_id)

    context = {
        'categorys' : categorys,
        'content' : content,
        'comments' : comments,
    }

    return render(request, 'blogs/comments.html', context)