
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from app.views import *



urlpatterns = [
  path('',home),
  path('home/',home,name='home'),
  path('login/',login,name='login'),
  path('signup/',signup),
  path('logout/',signout),
  path('add_todo/',add_todo),
  path('delete_todo/<int:id>',delete_todo),
  path('change-status/<int:id>/<str:status>',change_todo),
]
