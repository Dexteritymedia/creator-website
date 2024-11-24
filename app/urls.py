from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('home/', views.homepage),
    path('add-review/', views.add_review),
    path('budget/', views.budget_view, name='budget_view'),
    path('activities/', views.activities, name='activities'),
    path('get-suggestions/', views.get_suggestions, name='get_suggestions'),
]
