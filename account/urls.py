from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('register/sender/', views.RegisterSenderView.as_view()),
    path('register/buyer/', views.RegisterBuyerView.as_view()),

    path('token/', obtain_auth_token)
]
