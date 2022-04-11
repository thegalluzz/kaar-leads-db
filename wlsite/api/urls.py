from django.urls import path, include
from .views import *

urlpatterns = [
    path("contact-form/",
         ContactFormAPI.as_view(), name="contact-form"),
    path("auth/", include('rest_auth.urls')),
    path("auth/registration/", include('rest_auth.registration.urls')),
    path('webhook', Webhook),
    path("leads/", LeadAPI.as_view(), name="leads"),
    path("leads/<int:pk>/", LeadAPI.as_view(), name="leads-detail"),
]
