from django import forms
class ContactForm(forms.Form):
    ismi=forms.CharField(max_length=100)
    familiya=forms.CharField(max_length=100)
    elektron_pochta=forms.EmailField()
    tel_raqam=forms.IntegerField()
    txt=forms.CharField(max_length=1000)
class ContactForm2(forms.Form):
    ismi=forms.CharField(max_length=100)
    familiya=forms.CharField(max_length=100)
    elektron_pochta=forms.EmailField()
    phone=forms.IntegerField()
class ProfileForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput,max_length=100)
