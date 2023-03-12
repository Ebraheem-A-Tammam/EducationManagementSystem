from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm, CommentForm
from .models import Article


@login_required
def article_list_view(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "forums/article_list.html", context)


@login_required
def article_detail_view(request, article_id):
    article = Article.objects.get(id=article_id)
    form = CommentForm(request.POST or None)
    context = {"article": article, "form": form}
    if form.is_valid():
        obj1 = form.save(commit=False)
        obj1.author = request.user
        obj1.article = article
        obj1.save()
        context["form"] = CommentForm()
    return render(request, "forums/article_detail.html", context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {"form": form}
    if form.is_valid():
        obj1 = form.save(commit=False)
        obj1.author = request.user
        obj1.save()
        context["form"] = ArticleForm()
        context["created"] = True
        return redirect("/forums")
    return render(request, "forums/create_article.html", context)


@login_required
def article_update_view(request, article_id):
    obj = get_object_or_404(Article, id=article_id)
    form = ArticleForm(request.POST or None, instance=obj)
    context = {"form": form, "object": obj}
    if form.is_valid():
        form.save()
        return redirect("/forums")
    return render(request, "forums/update_article.html", context)
