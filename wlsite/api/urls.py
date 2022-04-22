from django.urls import path, include
from .views import *

urlpatterns = [
    path("contact-form/",
         ContactFormAPI.as_view(), name="contact-form"),
    path("auth/", include('rest_auth.urls')),
    path("auth/registration/", include('rest_auth.registration.urls')),
    path('webhook-ads/', WebhookAds),
    path('webhook-website/', WebhookWebsite),
    path('webhook-msn/', WebhookMSN),
    path('lead-ads/', LeadAdsAPI.as_view(), name="leads"),
    path('lead-ads/<int:pk>/', LeadAdsAPI.as_view(), name="leads-detail"),
]