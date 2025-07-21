from django.db import models
from django_jalali.db import models as jmodels
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255)
    caption=models.TextField()
    published_date=models.DateTimeField(blank=True,null=True)

    
    def __str__(self):
        return "{}-{}".format(self.title,self.id)



class Image_blog(models.Model):
    related_blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='Blogimages/')

    def __str__(self):
        return self.image.name
    


class Blog_persian(models.Model):
    title=models.CharField(max_length=255)
    caption=models.TextField()
    published_date=jmodels.jDateField(blank=True,null=True)

    
    def __str__(self):
        return "{}-{}".format(self.title,self.id)



class Image_blog_persian(models.Model):
    related_blog = models.ForeignKey(Blog_persian,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='Blogimages/')

    def __str__(self):
        return self.image.name