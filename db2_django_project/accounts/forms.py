from django import forms
from accounts.models import User


class UserRegistrationForm(forms.ModelForm):
    """
    Generate form with email, password1 and password2.
    """
    email = forms.EmailField(max_length=200, widget=forms.EmailInput(), help_text='Enter your email.')
    password1 = forms.CharField(min_length=8, max_length=40, widget=forms.PasswordInput(),
                                help_text='Enter your password.')
    password2 = forms.CharField(min_length=8, max_length=40, widget=forms.PasswordInput(),
                                help_text='Enter the same password as before, for verification.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def clean_email(self):
        # Email matching check

        try:
            User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("The email already exists. Please try another one.")

    def clean_password2(self):
        # Password matching check

        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn't match.")
        return password2


class UserLoginForm(forms.Form):
    """
    Login form with email and password fields.
    """
    email = forms.EmailField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
