from django.conf.urls import url
from userActivityRestApi import views

urlpatterns = [
    url(r'^users/', views.userList)
]
