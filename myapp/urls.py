from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('additional_step/', views.additional_step, name='additional_step'),  # Adjustments from step 3
]
