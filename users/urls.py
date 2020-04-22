from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('human/<int:pk>/', views.HumanDetailView.as_view(), name='detail'),
    path('human/create/', views.HumanCreateView.as_view(), name='operate'),
]
