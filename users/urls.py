from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('human/<int:pk>/', views.HumanRUDView.as_view(), name='rud'),
    path('human/', views.HumanListCreateView.as_view(), name='operate'),
]
