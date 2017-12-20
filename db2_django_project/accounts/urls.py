from django.urls import path, re_path
from accounts.views import Login, ActivationEmailSent, ActivateUser, UserRegistration, Logout

app_name = 'accounts'

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('activation_sent/', ActivationEmailSent.as_view(), name='activation_sent'),
    re_path(r'^activate/(?P<id>[0-9]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            ActivateUser.as_view(), name='activate'),
    path('logout/', Logout.as_view(), name='logout'),
]
