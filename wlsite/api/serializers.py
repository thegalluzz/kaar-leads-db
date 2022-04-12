from rest_framework import serializers

from .models import ContactForm, LeadAds

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'


class LeadAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadAds
        fields = '__all__'