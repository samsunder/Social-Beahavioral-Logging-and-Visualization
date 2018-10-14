from django import forms


class formsingup(forms.Form):
    First_Name = forms.CharField(max_length = 20, label="First Name")
    Last_Name = forms.CharField(max_length = 20, label="Last Name")
    Username = forms.CharField(max_length = 20, label="UserName")
    Password = forms.CharField(max_length = 20, label="Password")
    Email = forms.CharField(required=False, max_length = 20, label="Email")