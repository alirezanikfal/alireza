from django.contrib import admin
from .models import Article ,Category
from django.contrib import messages
from django.utils.translation import ngettext

# Register your models here.
admin.site.site_header = 'وبلاگ من'


# def make_published(modeladmin, request, queryset):
#     queryset.update(status='p')
#
# make_published.short_description = "انتشار مقاله"


def make_published(modeladmin, request, queryset):
    rows_updated = queryset.update(status='p')
    if rows_updated == 1:
        message_bit = "منتشر شد."
    else:
        message_bit = "منتشر شدند."
    modeladmin.message_user(request, "{} مقاله {}".format(rows_updated, message_bit))


make_published.short_description = "انتشار مقالات انتخاب شده"


class Article_Admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status', 'tag_image','Categoryes')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-publish']

    actions = [make_published]


admin.site.register(Article, Article_Admin)
admin.site.register(Category)
