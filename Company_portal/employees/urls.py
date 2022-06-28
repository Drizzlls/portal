from django.urls import path, include
from .views import UsersFromBitrix

urlpatterns = [
    path('', UsersFromBitrix.showListUsers),
    path('user/<int:idSotr>',UsersFromBitrix.profile,name="userProfile"),
    path('load',UsersFromBitrix.loadUsers)
]