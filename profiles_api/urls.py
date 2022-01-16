from django.db import router
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('user', views.UserProfileViewSet)
router.register('login',views.LoginViewSet,basename='login')

urlpatterns = [
    
  path('api/list/',views.HelloView.as_view(),name="listView"),
 path('',include(router.urls))
  
]
