from django.contrib import admin

# Register your models here.

from . models import Post, Tag, Comment

class PostAdmin(admin.ModelAdmin):
    # переопределение формата отображения поля даты в админке
    def date_format(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    # date_format.admin_order_field = 'date'
    date_format.short_description = 'Date' 

    list_display = ("title", "date_format", "excerpt")
    list_filter = ("tag", "date")
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    # переопределение формата отображения поля даты в админке
    def date_format(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    # date_format.admin_order_field = 'date'
    date_format.short_description = 'Date' 

    list_display = ("post", "comment", "date_format", "username", "usermail")
    list_filter = ("username", "date")


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
