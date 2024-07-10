from django.urls import path
from teams.views import TeamBase

urlpatterns = [
    path('', TeamBase.as_view(), name='get/createTeam'),
    path('<int:pk>/', TeamBase.as_view(), name='getspecificTeam'),
]
