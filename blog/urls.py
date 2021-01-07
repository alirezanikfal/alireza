from django.urls import path
from .views import Article_List, Aticle_Detail, Category_list, AuthorList

app_name = "blog"

urlpatterns = [
    path('', Article_List.as_view(), name='article_list'),
    path('page/<int:page>', Article_List.as_view(), name='article_list_page'),
    path('article/<slug:slug>', Aticle_Detail.as_view(), name='article_detail'),
    path('category/<slug:slug>', Category_list.as_view(), name='category'),
    path('category/<slug:slug>/page/<int:page>', Category_list.as_view(), name='category_page'),
    path('author/<username>', AuthorList.as_view(), name='authorarticle'),
    path('author/<username>/page/<int:page>', AuthorList.as_view(), name='authorarticle_page'),

]
