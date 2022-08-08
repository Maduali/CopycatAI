from django.db import models


class Registration(models.Model):

    CHOICES= (
        ('GO', 'GOVERMENT ORGANIZATION'),
        ('NGO', 'NON-GOVERNMENT ORGANIZATION'),
        ('OTH', 'PRIVATE COMPANY')
    )

    name_of_organization = models.CharField(max_length=1000)
    type_of_organization = models.CharField(max_length=1000, 
    choices= CHOICES)
    admin_email = models.EmailField(max_length=70,blank=True,unique=True)
    admin_whatsapp_number = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    keywords = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_text


    
class Locations(models.Model):
    name = models.TextField(max_length=255)


    def __str__(self):
        return self.question_text

