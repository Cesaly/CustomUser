from django.urls import path
from customuser import views

urlspatterns = [
    path('', views.index, name='home'),
    path('login/', views.signin),
    path('signup/', views.signup),
    path('logout/', views.signout)
]
