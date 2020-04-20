from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('human', views.HumanView.as_view(), name='operate'),
]
