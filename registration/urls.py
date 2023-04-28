from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("our_service", views.OurServiceView.as_view(), name="our_service"),
    path("monthly", views.MonthlySubscriptionView.as_view(), name="monthly-subscription"),
    path("annual", views.AnnualSubscriptionView.as_view(), name="annual-subscription"),
    path("semi-annual", views.SemiAnnualSubscriptionView.as_view(), name="semi-annual-subscription"),
    path("create-subscription", views.create_subscription, name="create-subscription"),
    # path('signup/', views.SignupView.as_view(), name='account_signup'),
    # path('login/', views.LoginView.as_view(), name='account_login'),
    # path('logout/', views.LogoutView.as_view(), name='account_logout'),
    # path('profile/', views.ProfileView.as_view(), name='account_profile'),
]
