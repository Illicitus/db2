from django.views import View
from django.views.generic import TemplateView

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import login, authenticate, logout

from django.shortcuts import render, redirect
from django.template import loader

from accounts.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm
from accounts.tokens import account_activation_token


class Login(View):
    """
    GET - return login form.
    POST - check user form data and login in system it data is correct.
    """
    form_class = UserLoginForm
    template_name = 'login.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                return redirect('blog:home')

            else:
                data = form.cleaned_data
                user = authenticate(email=data.get('email'), password=data.get('password'))

                if user:
                    login(self.request, user)
                    return redirect('blog:home')

                else:
                    return render(request, self.template_name, {'form': form})
        else:
            return render(request, self.template_name, {'form': form})


class UserRegistration(View):
    """
    GET - return registration form.
    POST - generate and send email to new user with activation link.
    """

    form_class = UserRegistrationForm
    template_name = 'registration.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        # Check form validation
        if form.is_valid():
            data = form.cleaned_data

            # Create user
            user = User.objects.create(
                email=data.get('email')
            )
            user.set_password(data.get('password2'))
            user.is_active = False
            user.save()

            # Generate and send letter to user email
            current_site = get_current_site(request)
            subject = 'Activate Your Account'

            message = loader.render_to_string('activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'id': user.pk,
                'token': account_activation_token.make_token(user),
                'protocol': 'http',
            })

            user.email_user(subject, message)

            return redirect('accounts:activation_sent')

        else:
            return render(request, self.template_name, {'form': form})


class ActivationEmailSent(TemplateView):
    """
    Return template with success text.
    """
    template_name = 'activation_sent.html'


class ActivateUser(View):
    """
    Change user status to active if token is right.
    """

    def get(self, request, id, token):
        try:
            user = User.objects.get(pk=id)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.email_confirmed = True
            user.save()

            login(request, user)
            return redirect('blog:home')

        else:
            return render(request, 'activation_invalid.html')


class Logout(View):
    """
    Logout user from system and redirect to "accounts:login'.
    """
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('accounts:login')

        else:
            return redirect('accounts:login')
