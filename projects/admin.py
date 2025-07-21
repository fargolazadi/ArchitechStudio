from django.contrib import admin
from projects.models import *
from jalali_date.admin import ModelAdminJalaliMixin
# Register your models here.

class imageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ['image']


class ProjectAdmin(admin.ModelAdmin):

    inlines = [imageInline]




class image_persianInline(admin.TabularInline):
    model = Image_persian
    extra = 1
    fields = ['image']


class Project_persianAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):

    inlines = [image_persianInline]

admin.site.register(Project,ProjectAdmin)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Status)


admin.site.register(Project_persian,Project_persianAdmin)
admin.site.register(Image_persian)
admin.site.register(Category_persian)
admin.site.register(Status_persian)
