from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
import datetime
class RegistrationUserForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True, label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))


    email = forms.EmailField(label='Email', required=True)
    first_name = forms.CharField(label='Имя', required=False, max_length=25)
    last_name = forms.CharField(label="Фамилия", required=False, max_length=25)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name',)
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-input'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-input'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-input'}),
                   }


    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('На этот электронный адрес зарегистрирован аккаунт')
        return email


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True, label='Логин/E-mail',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(max_length=20, required=True, label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class ProfileUserForm(forms.ModelForm): 
    username = forms.CharField(disabled=True, label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-input'}))
    this_year = datetime.date.today().year
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(this_year-100, this_year-5)),
                                    label = 'Дата рождения')

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'photo', 'date_of_birth']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'photo': 'Фото',
            'date_of_birth': 'Дата рождения',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }
class UserPasswordChangeForm(PasswordChangeForm):

    old_password = forms.CharField(max_length=20, required=True, label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(max_length=20, required=True, label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(max_length=20, required=True, label='Повторите новый пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
