from rest_framework import generics
from rest_framework.response import Response
from .serializer import DoctorSerializer, UsersSerializer
from .models import Doctor, Users


class DoctorCreateApi(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorApi(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDeleteApi(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class UsersCreateApi(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersApi(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UsersDeleteApi(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
