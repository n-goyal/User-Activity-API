# from django.conf.urls import url
from django.urls import path
from userActivityRestApi import views

urlpatterns = [
    path('', views.getHomePage),
    path('api/v1/users/', views.userList),
    # path('api/v1/user/<str:id>', views.getUser)
]
