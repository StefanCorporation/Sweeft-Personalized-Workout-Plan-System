from django.urls import path
from trainings import views

app_name = 'trainings'

urlpatterns = [
    path('trainings/', views.IndexView.as_view(), name='index')
]
