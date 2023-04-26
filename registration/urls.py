from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('our_service', views.OurServiceView.as_view(), name='our_service'),
    # path('signup/', views.SignupView.as_view(), name='account_signup'),
    # path('login/', views.LoginView.as_view(), name='account_login'),
    # path('logout/', views.LogoutView.as_view(), name='account_logout'),
    # path('profile/', views.ProfileView.as_view(), name='account_profile'),
]
