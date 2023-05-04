from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key='True')
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=70)

    # Return student name as string
    def __str__(self):
        # Return student ID (int number)
        return self.name

    '''Return student ID
    def __str__(self):
        # Return student ID (int number)
        return str(self.id)'''
