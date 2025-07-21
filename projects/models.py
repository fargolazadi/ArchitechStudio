from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Status(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value
    

class Project(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    category = models.ManyToManyField(Category)
    status_value = models.ManyToManyField(Status)
    TYPE_CHOICES = [
        ('commercial', 'Commercial'),
        ('villa', 'Villa'),
        ('apartment', 'Apartment'),
        ('residential-co', 'Residetial complex'),
        ('renovation', 'Renovation'),
        ('industrial', 'Industrial'),
        ('public-space', 'Public space'),
    ]
    type = models.CharField(max_length=14,choices=TYPE_CHOICES)

    STATUS_CHOICES=[
        ('Completed','completed'),
        ('Concept','concept'),
        ('in progress','In progress'),
    ]
    status = models.CharField(max_length=11,choices=STATUS_CHOICES)
    design_year = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100)
    client = models.CharField(max_length=80)
    team = models.CharField(max_length=255)
    architects = models.CharField(max_length=100,default='mobina shafiei')
    constructor = models.CharField(max_length=100)
    scale = models.FloatField(default=100)
    VR_html = models.FileField(upload_to='VRhtmlfiles/', blank=True, null=True)
    

    def __str__(self):
        return "{}-{}".format(self.title,self.id)


class Image(models.Model):
    related_project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='projectimages/')


    def __str__(self):
        return self.image.name
    


class Category_persian(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Status_persian(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value
    

class Project_persian(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    category = models.ManyToManyField(Category_persian)
    status_value = models.ManyToManyField(Status_persian)
    TYPE_CHOICES = [
        ('تجاری', 'تجاری'),
        ('ویلا', 'ویلا'),
        ('آپارتمان', 'آپارتمان'),
        ('مجتمع مسکونی', 'مجتمع مسکونی'),
        ('بازسازی', 'بازسازی'),
        ('صنعتی', 'صنعتی'),
        ('فضای عمومی', 'فضای عمومی'),
    ]
    type = models.CharField(max_length=20,choices=TYPE_CHOICES)

    STATUS_CHOICES=[
        ('تکمیل','تکمیل'),
        ('ایده','ایده'),
        ('در حال اجرا','در حال اجرا'),
    ]
    status = models.CharField(max_length=20,choices=STATUS_CHOICES)
    design_year = jmodels.jDateField(blank=True,null=True)
    location = models.CharField(max_length=100)
    client = models.CharField(max_length=80)
    team = models.CharField(max_length=255)
    architects = models.CharField(max_length=100,default='mobina shafiei')
    constructor = models.CharField(max_length=100)
    scale = models.FloatField(default=100)
    VR_html = models.FileField(upload_to='VRhtmlfiles/', blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.title,self.id)


class Image_persian(models.Model):
    related_project = models.ForeignKey(Project_persian,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='projectimages/')


    def __str__(self):
        return self.image.name
    

