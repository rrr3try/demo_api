from django.urls import path

from match import views

app_name = 'match'

urlpatterns = [
    path('match/<int:human_id>/', views.MatchDetailView.as_view(), name='detail'),
    path('match/', views.MatchListView.as_view(), name='list'),
]
