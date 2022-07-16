from django.urls import path, include
from .views import *

urlpatterns = [
    path('', UsersFromBitrix.showListUsers,name="ListUsers"),
    path('user/<int:idSotr>',UsersFromBitrix.profile,name="userProfile"),
    path('load',UsersFromBitrix.loadUsers),
    path('add',addPerson,name='AddPerson'),
    path('registration',registrationUser,name='RegUser')
]
