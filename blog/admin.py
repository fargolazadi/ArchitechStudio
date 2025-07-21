from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin
# Register your models here.

from .models import *

class Image_blogInline(admin.TabularInline):
    model = Image_blog
    extra = 1
    fields = ['image']


class BlogAdmin(admin.ModelAdmin):

    inlines=[Image_blogInline]


admin.site.register(Blog,BlogAdmin)
admin.site.register(Image_blog)


class Image_blog_persianInline(admin.TabularInline):
    model = Image_blog_persian
    extra = 1
    fields = ['image']


class Blog_persianAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):

    inlines = [Image_blog_persianInline]


admin.site.register(Blog_persian,Blog_persianAdmin)
admin.site.register(Image_blog_persian)