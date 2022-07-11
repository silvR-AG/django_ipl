from django.urls import path
from . import views

urlpatterns = [
    # path('matchplayed/', views.matches_per_year),
    path('matchesplayed/', views.matches_per_year),
    path('matcheswon/', views.matches_won),
    path('extraruns/', views.extra_runs),
    path('econbowl/',views.econ_bowler)
    
]