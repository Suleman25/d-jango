
from django.urls import path
from firstapp import views
urlpatterns = [
    path('january/' , views.jan),
    path('february/' , views.feb),
]