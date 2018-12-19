from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('index', views.index, name = "index"),
    path('new', views.new, name = "new"),
    path('update/<int:id>', views.update, name = "update"),
    path('delete/<int:id>', views.delete, name = "delete"),
    path('login', views.userLogin, name = "login"),
    path('signup', views.signup, name = "signup"),
    path('logout', views.logout, name = "logout"),
]