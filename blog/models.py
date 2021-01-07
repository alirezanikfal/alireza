from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from extion.utlis import jalali_converter


# Create your models here


class Article_Manage(models.Manager):
    def published(self):
        return self.filter(status='p')


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='عنوان ادرس')


    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOICES = (
        ('p', 'انتشار یافت'),
        ('d', 'پیش نویس')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=150, verbose_name='عنوان')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='عنوان ادرس')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to='image', verbose_name='عکس')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    category = models.ManyToManyField(Category,related_name='articles',verbose_name='دسته بندی')

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jtim(self):
        return jalali_converter(self.publish)

    def tag_image(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.image.url))

    tag_image.short_description = 'عکس'

    def Categoryes(self):

        return ",".join([cat.title for cat in self.category.all()])

    Categoryes.short_description = 'دسته بندی'

    objects = Article_Manage()
