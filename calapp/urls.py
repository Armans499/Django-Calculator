
from django.urls import path
from . import views

urlpatterns = [
   path('sample/',views.sample),
   path('calculate/', views.calculate),
]