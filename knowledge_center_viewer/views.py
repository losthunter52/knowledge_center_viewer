from django.shortcuts import render
from knowledge_center_viewer.models import Article
import pandas as pd 

def index(request):
    articles = Article.objects.all()
    new_articles = Article.objects.filter(status="new")
    new_count = new_articles.count()
    doing_articles = Article.objects.filter(status="doing")
    doing_count = doing_articles.count()
    done_articles = Article.objects.filter(status="done")
    done_count = done_articles.count()
    context = {
        'articles': articles,
        'new_articles' : new_articles,
        'new_count': new_count,
        'doing_articles': doing_articles,
        'doing_count' : doing_count,
        'done_articles': done_articles,
        'done_count': done_count
    }
    return render(request, 'index.html', context)

def update_database(request):
    df = pd.read_csv('arquivo.csv')
    for index, row in df.iterrows():
        body = row['Article body']
        title = row['Article title']    
        article = Article(title=title, body=body)
        article.save()
    return render(request, 'index.html')

def edit_article(request, pk):
    if request.method == "POST":
        article = Article.objects.get(pk=pk)
        article.comment = request.POST.get('comment')
        article.status = request.POST.get('status')
        article.hot = "false"
        article.save()

    article = Article.objects.get(pk=pk)
    articles = Article.objects.all()
    new_articles = Article.objects.filter(status="new")
    new_count = new_articles.count()
    doing_articles = Article.objects.filter(status="doing")
    doing_count = doing_articles.count()
    done_articles = Article.objects.filter(status="done")
    done_count = done_articles.count()
    status_list = ['new', 'doing', 'done']
    context = {
        'article': article,
        'articles': articles,
        'new_articles' : new_articles,
        'new_count': new_count,
        'doing_articles': doing_articles,
        'doing_count' : doing_count,
        'done_articles': done_articles,
        'done_count': done_count,
        'status_list' : status_list,
    }
    return render(request, 'article.html', context)