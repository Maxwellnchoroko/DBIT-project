from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number= models.CharField(max_length=10)
    needed_expertise = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.first_name
    def __int__(self):
        return self.pub_date
    def __str__(self):
        return self.needed_expertise

   

class Player(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number= models.CharField(max_length=10)
    area_of_specilisation=models.CharField(max_length= 200)
    pub_date = models.DateTimeField(auto_now_add=True)
       
       
       
    def __str__(self):
        return self.first_name
    def __int__(self):
        return self.pub_date
    def __str__(self):
        return self.area_of_specilisation
    # class Meta:
    #     ordering = ['first_name']