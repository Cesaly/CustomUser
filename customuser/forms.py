from django import forms


class SignInForm(forms.Form):
    username = forms.CharField(max_length=30)
    passsword = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30)
    passsword = forms.CharField(widget=forms.PasswordInput)
    homepage = forms.URLField(max_length=100, required=False)
    age = forms.IntegerField(required=False)
    display_name = forms.CharField(max_length=40)
