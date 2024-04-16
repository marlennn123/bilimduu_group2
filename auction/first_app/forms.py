from allauth.account.forms import SignupForm, LoginForm
from django import forms


class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Имя')
    last_name = forms.CharField(max_length=30, label='Фамилия')
    age = forms.IntegerField(label="Возраст")
    country = forms.CharField(max_length=30, label='Страна')

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)

        del self.fields['username']

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.age = self.cleaned_data['age']
        user.country = self.cleaned_data['country']
        user.save()
        return user