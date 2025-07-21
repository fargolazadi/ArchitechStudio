from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['published_date']

    def __str__(self):
        return "{}-{}".format(self.name,self.subject)
