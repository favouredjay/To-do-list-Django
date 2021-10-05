from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add/', views.add, name='task'),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("delete/<int:pk>", views.delete, name="delete_task")

    # path('delete/', views.delete)
]
