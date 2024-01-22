from django.urls import path
from . import views
from .views import telegramView, create_subActive, save_telegram

#app_name = 'telegram'

urlpatterns = [
    #path("", views.telegramView.as_view(), name="telegram"),
    path("telegram-checkout", views.telegramView.as_view(), name="telegram_checkout"),
    path('create-subactive', views.create_subActive.as_view(), name='create-subactive'),
    #path('form-subactive', views.FormSubactive, name='form-subactive'),
    path('save-telegram', save_telegram, name='save-telegram'),
]