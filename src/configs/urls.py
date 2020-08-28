from django.contrib import admin
from django.urls import path, include

from botapp import views


urlpatterns = [
    path('bot/', views.handle_request),
    path('', include('webapp.urls'))    
]
