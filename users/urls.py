from django.urls import path
from django.contrib.auth.views import LogoutView

from users import views




app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]