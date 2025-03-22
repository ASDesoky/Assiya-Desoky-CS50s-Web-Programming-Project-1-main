from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Index view
    path('wiki/<str:title>/', views.entry, name='entry'),  # Entry view
    path('new/', views.new_entry, name='new_entry'),  # New entry view
    path("edit/<str:title>/", views.edit_entry, name="edit_entry"),  # Edit view
    path('random/', views.random_page, name='random_page'),  # Random page view
    path('search/', views.search, name='search'),  # Search view
    path('delete/<str:title>/', views.delete_entry, name='delete_entry'),  # Delete entry
]
