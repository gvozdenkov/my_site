from django.urls import path

# импортировать из текущей директории файл views с отображениями адресов
from . import views

# urls приложения
urlpatterns = [
    path('', views.BlogHomeView.as_view(), name="blog-home"),
    # path('posts', views.posts, name="posts-page"),
    
    # slug - любое переменное текстовое значение, например posts/my-first-post
    # path('posts/<slug:slug>', views.post_detail, name="post-detail-page"),
]