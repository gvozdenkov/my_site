import datetime

from django.db import models


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Post(models.Model):
    image = models.ImageField(upload_to="post_img")
    title = models.CharField(max_length=40)
    excerpt = models.CharField(max_length=120)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return f"{self.title} ({self.date.strftime('%d.%m.%Y')})"

    class Meta:
        # для отображения в админке
        verbose_name_plural = "Posts"

class Comment(models.Model):
    username = models.CharField(max_length=30)
    usermail = models.EmailField(max_length=50)
    comment = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)

    # Many to One зависимость. Много комментов для одного поста. 
    # Каскадное удаление = если удаляется пост, то удаляются и комменты
    # related_name - через него можно дотянуться из объекта Post до всех связанных с ним Comment
    # related_name как контекст во views.py используем
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")