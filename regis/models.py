from django.db import models
from django import forms
# Create your models here.
class database(models.Model):
    first_name=models.CharField(max_length=255,blank=False,null=False)
    last_name=models.CharField(max_length=255,blank=False,null=False)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)

    
class register_form(forms.ModelForm):
    error_messages = {
    'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput())
    password2=forms.CharField(label=("Password Comfirmation"),widget=forms.PasswordInput(), help_text=("Enter the same password as above, for verification."))
    class Meta:
        model=database
        fields=['first_name','last_name','email']
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2
    def save(self,commit=True):
        user=super(forms.ModelForm, self).save(commit=False)
        user.password=self.cleaned_data.get("password1")
        if commit:
            user.save()
        return user

