from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', views.index),
    path('home/', views.homepage),
    path('add-review/', views.add_review),
    path('budget/', views.budget_view, name='budget_view'),
    path('search/', views.search_view, name='search_view'),
    path('search/results/', views.search_results_view, name='search_results_view'),
    path('activity/<pk>/', views.edit_activity, name='edit_activity'),
    path('activities/', views.activities, name='activities'),
    path('get-suggestions/', views.get_suggestions, name='get_suggestions'),

    path('service-worker.js', TemplateView.as_view(template_name="service-worker.js", content_type='application/javascript')),
]
