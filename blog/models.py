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
        return f"{self.title} ({self.date.strftime('%d-%m-%Y')}) -> {self.excerpt[:15]}"

    class Meta:
        # для отображения в админке
        verbose_name_plural = "Posts"
