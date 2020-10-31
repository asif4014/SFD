from django.db import models

# Create your models here.
# class Students(models.Model):
#     name = models.CharField(max_length=100)
#     course = models.CharField(max_length=100)
#     regdno = models.CharField(max_length=100)


#     def __str__(self):
#         return self.name

class Users(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    regdno = models.CharField(max_length=100)
    password = models.CharField(max_length =100)
    

    def __str__(self):
        return self.name

class StuDetails(models.Model):
    name = models.CharField(max_length=100)
    regdno = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.DateField()
    scholartype = models.CharField(max_length=10)
    aadhar = models.IntegerField()
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name