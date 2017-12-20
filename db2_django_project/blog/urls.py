from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('/', Login.as_view(), name='login'),
]
