from django import forms
from .models import DEPARTMENT, Orders,OrderItems

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['CompanyName','Deadline','DEPARTMENT','Comment','TotalPrice']