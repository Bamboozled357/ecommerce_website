from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, get_object_or_404, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
import json
from .models import MyUser
from .serializers import RegisterSerializer


class RegisterSenderView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.save(is_sender=True)


class RegisterBuyerView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = RegisterSerializer
