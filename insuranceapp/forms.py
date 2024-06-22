# forms.py
from django import forms
from .models import Agent, Customer
from .models import Policy

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name']  # Add other fields as necessary

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'date_of_birth', 'age', 'phone', 'address', 'aadhar_card_number', 'pan_card_number']





class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['policy_number', 'customer_name', 'agent', 'status']
