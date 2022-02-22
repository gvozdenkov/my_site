from pyexpat import model
from django import forms

from . models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields - включает поля модели в форму
        # exclude - исключает из отображения формы указанные поля
        # fields = ["username", "usermail", "comment"]
        exclude = ["date", "post"]
        
        # подписи к полям
        labels = {
            "username": "Enter your name",
            "usermail": "Enter your mail",
            "comment": "Your comment"
        }