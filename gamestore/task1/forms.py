from django import forms


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:', required=True)
    balance = forms.DecimalField(label='Введите баланс', required=True)
    age = forms.IntegerField(label='Введите свой возраст:', required=True)
