from django.urls import path
from market import views

urlpatterns = [
     path('createstore/', views.createstore),

]