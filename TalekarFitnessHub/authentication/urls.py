from django.urls import path
from authentication import views
urlpatterns = [
    path('',views.Home,name="Home"),
    path('signup',views.signup,name='signup'),
    path('handlelogin',views.handlelogin,name='handlelogin'),
    path('logout',views.logout,name='logout')
]
