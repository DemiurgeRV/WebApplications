from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.getFilters, name='Home'),
    path('filter/<int:id>/', views.getFilter, name='filter_url')
]
