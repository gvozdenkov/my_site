from django.contrib import admin

# Register your models here.

from . models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    # переопределение формата отображения поля даты в админке
    def date_format(self, obj):
        return obj.date.strftime("%d.%m.%Y")
    # date_format.admin_order_field = 'date'
    date_format.short_description = 'Date' 

    list_display = ("title", "date_format", "excerpt")
    list_filter = ("tag", "date")
    prepopulated_fields = {"slug": ("title",)}



admin.site.register(Post, PostAdmin)
admin.site.register(Tag)