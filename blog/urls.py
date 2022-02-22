from django.urls import path

# импортировать из текущей директории файл views с отображениями адресов
from . import views

# urls приложения
urlpatterns = [
    path('', views.BlogHomeView.as_view(), name="blog_home"),
    path('posts', views.AllPostsView.as_view(), name="all_posts"),
    
    # slug - любое переменное текстовое значение, например posts/my-first-post
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name="post-detail"),
]