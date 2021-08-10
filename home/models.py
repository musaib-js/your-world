from django.db import models

class Services(models.Model):
    sno = models.AutoField(primary_key = True)
    servicename = models.CharField(max_length = 60)
    slug = models.CharField(max_length = 150, default = "")
    servicedesc = models.TextField()
    serviceimg = models.ImageField(upload_to = 'media', default="")

    def __str__(self):
        return self.servicename

class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    phone = models.IntegerField()
    email = models.EmailField(max_length = 60)
    concern = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.name
