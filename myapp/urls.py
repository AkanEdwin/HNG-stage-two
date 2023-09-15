from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('persons-list/', views.personsList, name="persons-list"),
    path('persons-detail/<str:pk>/', views.personsDetail, name="persons-detail"),
    path('persons-create/', views.personsCreate, name="persons-create"),
    path('persons-update/<str:pk>/', views.personsUpdate, name="persons-update"),
    path('persons-delete/<str:pk>/', views.personsDelete, name="persons-delete"),
]