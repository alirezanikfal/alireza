from django.urls import path,include
from .views import home,Login

app_name = 'account'


urlpatterns = [
   path('login',Login.as_view(),name='login'),
   path('home',home,name='home'),
]
