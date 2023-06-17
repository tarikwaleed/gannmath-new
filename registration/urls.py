from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("our_service", views.OurServiceView.as_view(), name="our_service"),
    #################### Paypal Subscriptions ###############################
    path("monthly", views.MonthlySubscriptionView.as_view(), name="monthly-subscription"),
    path("annual", views.AnnualSubscriptionView.as_view(), name="annual-subscription"),
    path("semi-annual", views.SemiAnnualSubscriptionView.as_view(), name="semi-annual-subscription"),
    path("create-subscription", views.create_subscription, name="create-subscription"),
    path('calculate/', views.CalculateView.as_view(), name='calculate'),
    #################### Paypal Standard Checkout ###############################
    path("monthly-standard-checkout", views.MonthlyStandardCheckoutView.as_view(), name="monthly-standard-checkout"),
    path("semi-annual-standard-checkout", views.SemiAnnualStandardCheckoutView.as_view(), name="semi-annual-standard-checkout"),
    path("annual-standard-checkout", views.AnnualStandardCheckoutView.as_view(), name="annual-standard-checkout"),
    path("save-subscription", views.save_subscription, name="save-subscription"),
    path('spx/', views.SpxView.as_view(), name='spx'),
    # path('signup/', views.SignupView.as_view(), name='account_signup'),
    # path('login/', views.LoginView.as_view(), name='account_login'),
    # path('logout/', views.LogoutView.as_view(), name='account_logout'),
    # path('profile/', views.ProfileView.as_view(), name='account_profile'),
]
