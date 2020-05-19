from django.db import models

# Create your models here.


class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class student(models.Model):
    username= models.CharField(max_length=200,null=True)
    email=models.EmailField(null=True)
    password1=models.CharField(max_length=20,null=True)
    password2=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.username



