from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Article, Category


# Create your views here.


# def home(request):
#     article = Article.objects.published()
#     context = {
#         'article': article
#
#     }
#     return render(request,'blog/base.html',context)


class Article_List(ListView):
    queryset = Article.objects.published()
    template_name = 'blog/BLBL/Article_list.html'

    paginate_by = 1


class Aticle_Detail(DetailView):
    template_name = 'blog/BLBL/article.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.published(), slug=slug)

        return article


class Category_list(ListView):
    template_name = 'blog/BLBL/category.html'
    paginate_by = 1

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        article_catgory = category.articles.published()
        return article_catgory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class AuthorList(ListView):
    template_name = 'blog/BLBL/author.html'
    paginate_by = 1

    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User,username=username)
        article_author = author.articles.published()
        return article_author

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = author
        return context
