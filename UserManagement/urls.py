"""SchoolOfSoftware URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from UserManagement import views
from rest_framework import routers
<<<<<<< HEAD
# import django_cas

router = routers.DefaultRouter()
router.register('users/', views.UserViewSet)
router.register('userLoginLogs/', views.UserLoginLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.UserLoginAPIView.as_view()),
    # path('login/', django_cas.views.login),
    # path('logout/', django_cas.views.logout),
=======
import django_cas

router = routers.DefaultRouter()
router.register('/', views.LoginViewSet)

urlpatterns = [
    path('login/', django_cas.views.login),
    path('logout/', django_cas.views.logout),
>>>>>>> 9ec56b0552ed3ae9bb5351c316795c332c080acb

]
