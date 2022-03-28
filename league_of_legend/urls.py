from django.urls import path
from league_of_legend import views

app_name = 'league_of_legend'

urlpatterns = [
    path('hi_senna/', views.senna, name='hi_senna'),
    path('hi_yone/', views.yone, name = 'hi_yone'),


]