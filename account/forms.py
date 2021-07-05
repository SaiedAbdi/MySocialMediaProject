from account import models
from django import forms
from .models import Profile
messages = {
    'required' : 'این قسمت الزامی است',
    'invalid' : 'یک آدرس ایمیل معتبر وارد کنید',
}

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Enter Your Username'}))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs= {'class':'form-control', 'placeholder':'Enter Your Password'}))

class UserRegistrationForm(forms.Form):
    username = forms.CharField(error_messages=messages,max_length=30, widget=forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Enter Your Username'}))
    email = forms.EmailField(error_messages=messages,max_length=50, widget=forms.EmailInput(attrs= {'class':'form-control', 'placeholder':'Enter Your Email'}))
    password = forms.CharField(error_messages=messages,max_length=40, widget=forms.PasswordInput(attrs= {'class':'form-control', 'placeholder':'Enter Your Password'}))


class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Profile
        fields = ('bio','age')

class PhoneLoginForm(forms.Form):
    phone = forms.IntegerField()

    def clean_phone(self):
        phone = Profile.objects.filter(phone=self.cleaned_data['phone'])
        if not phone.exists():
            raise forms.ValidationError('This Phone Does not Exist')
        return self.cleaned_data['phone']
