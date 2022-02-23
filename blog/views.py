from urllib import request
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View

from . models import Post
from . forms import CommentForm

# Create your views here.

class BlogHomeView(ListView):
    template_name = "blog/blog-home.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        latest_posts = queryset[:3]
        return latest_posts

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

# рендер темплейта на основе DetailView
# class PostDetailView(DetailView):
#     model = Post
#     template_name = "blog/post-detail.html"
#     # это имя будет в темплейте html исользоваться для доступа к полям модели
#     context_object_name = "post"

#     # получение данных из связанной модели (таблицы базы) Tag
#     # через переопределение функции get_context_data
#     # .tag.all() - доступ к полю tag модели Post
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # получаем все tag из связанной модели
#         context["post_tags"] = self.object.tag.all()

#         # созадём форму для комментов. Передаём в темплейт для рендера
#         context["comment_form"] = CommentForm()
#         return context



class PostDetailView(View):
    def get(self, request, slug):
        # получаем объект Post по ключу slug, который приходит из url.py
        post = Post.objects.get(slug=slug)

        # добавляем контекст для темплейта (вместо переопределения get_context_data для DetailView)
        context = {
            "post": post,
            "post_tags": post.tag.all(),
            "comment_form": CommentForm(),
            # используем related_name из модели Comment, чтобы дотянуться до всех комментов к посту
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        # получаем объект Post для которого рендерится темплейт
        post = Post.objects.get(slug=slug)

        # форма с содержимым, чтобы не удалялось в случае ошибки
        form = CommentForm(request.POST)
        if form.is_valid():
            # если форма заполнена верно, нам нужно добавить поле post
            # чтобы объект Comment был связан с объектом Post (для которого коммент написан)
            # commit=False чтобы не сохранять в базу, а создать временный объект
            comment = form.save(commit=False)
            
            # добавляем поле post к объекту Comment - ссылка на текущий объект Post
            comment.post = post
            
            comment.save()

            # возврат на туже страницу (redirect)
            # reverse позволяет задать адрес не жёстко, а через name в url.py
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))

        # в случае ошибки в форме возвращаем форму, как в get(), но с исходными данными
        context = {
            "post": post,
            "post_tags": post.tag.all(),

            # тут не CommentForm, чтобы сохранить поля ввода при перезагрузке
            "comment_form": form,

            # используем related_name из модели Comment, чтобы дотянуться до всех комментов к посту
            "comments": post.comments.all()
        }
        return render(request, "blog/post-detail.html", context)