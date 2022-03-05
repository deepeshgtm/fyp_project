from django.urls import path, include
from core import views
from .api import DoctorCreateApi, DoctorApi, DoctorUpdateApi, DoctorDeleteApi, UsersApi, UsersCreateApi, UsersUpdateApi, UsersDeleteApi
urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('api/doctors', DoctorApi.as_view()),
    path('api/create/doctor', DoctorCreateApi.as_view()),
    path('api/<int:pk>/update/doctor', DoctorUpdateApi.as_view()),
    path('api/<int:pk>/delete/doctor', DoctorDeleteApi.as_view()),
    path('api/users', UsersApi.as_view()),
    path('api/create/users', UsersCreateApi.as_view()),
    path('api/<int:pk>/update/users', UsersUpdateApi.as_view()),
    path('api/<int:pk>/delete/users', UsersDeleteApi.as_view()),

]