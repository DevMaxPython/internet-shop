from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, SetPasswordForm
from .models import User
from django.core.exceptions import ValidationError


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')
        widgets = {
             'username': forms.TextInput(attrs={'class': 'input_field'}), 
             'password1': forms.PasswordInput(attrs={'class': 'input_field'})
        }


class RegistrationForm(UserCreationForm):
    password2 = forms.CharField(required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')
        widgets = {
             'email': forms.EmailInput()
        }


class ChangeUserForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('username', 'date_of_birth', 'email', 'avatar')
        widgets = {
             'username': forms.TextInput(attrs={'class': 'input_form_profile'}), 
             'date_of_birth': forms.DateInput(attrs={'class': 'input_form_profile'}), 
             'email': forms.EmailInput(attrs={'class': 'input_form_profile'}), 
             'avatar': forms.FileInput(attrs={'class': 'input_form_profile'})
        }

        def __init__(self, *args, **kwargs):
            super(ChangeUserForm, self).__init__(*args, **kwargs)
            self.fields['avatar'].widget.clearable_file_input = False
        
        

    


class ChangePasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': ('Пароли не совпадают.'),
        'min_len': ('Минимальная длина 6 символов.'),
    }

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                    ValidationError(
                    self.error_messages['Пароли не совпадают'],
                    code='password_mismatch',
                )
            if len(password1) and len(password2) < 6:
                    ValidationError(
                    self.error_messages['Минимальная длина 6 символов'],
                    code='min_len',
                )
        return password2
    class Meta:
        model = User
        

