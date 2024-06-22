# models.py
from django.db import models
class Agent(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)  # Ensure unique constraint at the database level


    def __str__(self):
        return self.name

class Customer(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    aadhar_card_number = models.CharField(max_length=20)
    pan_card_number = models.CharField(max_length=20)
    # Add more fields as needed for customer details

    def __str__(self):
        return self.name


class Policy(models.Model):
    policy_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('canceled', 'Canceled'),
    ], default='active')

    def __str__(self):
        return self.policy_number
