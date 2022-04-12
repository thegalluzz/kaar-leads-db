from django.shortcuts import render
from django.http import HttpResponse, response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from .serializers import ContactFormSerializer, LeadAdsSerializer
from .models import ContactForm, LeadAds, LeadWebsite
import json

class ContactFormAPI(APIView):

    def post(self, request):
        serializer = ContactFormSerializer(data=request.data)

        if serializer.is_valid():
            first_name = serializer.validated_data.get(
                'first_name')
            last_name = serializer.validated_data.get(
                'last_name')
            email = serializer.validated_data.get(
                'email')
            phone = serializer.validated_data.get(
                'phone')
            country = serializer.validated_data.get(
                'country')
            details = serializer.validated_data.get(
                'details')

            try:
                send_mail(
                    from_email=email,
                    subject=first_name + ' ' + last_name +
                    ' ' + str(datetime.now()),
                    message=details,
                    recipient_list=[settings.EMAIL_ADMIN],
                    fail_silently=False,
                )
            except Exception as e:
                print(e)
                return Response({"Error": {"code": 500, "message": "email send error"}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class LeadAdsAPI(APIView):
    """
    List all Leads, or create a new Lead.
    """
    def get(self, request, format=None):
        lead_ads = LeadAds.objects.all()
        serializer = LeadAdsSerializer(lead_ads, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeadAdsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def WebhookAds(request):
    if request.method == 'POST':
        #print("Data received from Webhook is: ", request.body)


        test = request.body.decode('utf-8')
        test = json.loads(test)

        print(test)
        changes = test['entry'][0]['changes']
        print(changes)

        ad_id = test['entry'][0]['changes'][0]['value']['ad_id']
        form_id = test['entry'][0]['changes'][0]['value']['form_id']
        leadgen_id = test['entry'][0]['changes'][0]['value']['leadgen_id']
        created_time = test['entry'][0]['changes'][0]['value']['created_time']
        page_id = test['entry'][0]['changes'][0]['value']['created_time']
        adgroup_id = test['entry'][0]['changes'][0]['value']['created_time']

        LeadAds.objects.create(
            lead_id = leadgen_id,
            created_time = created_time,
            ad_id = ad_id,
            ad_name = 'ad_name',
            adset_id = 'adset_id',
            adset_name = 'adset_name',
            campaign_id = 'campaign_id',
            campaign_name = 'campaign_name',
            form_id = form_id,
            full_name = 'full_name',
            phone_number = 'phone_number',
            email = 'email',
            car_request = 'adgroup_name'
            )

        #for element in test['entry']:
            #Lead.objects.create(name="test", get_from_facebook=element['id'])
        
    return HttpResponse(request.GET.get("hub.challenge"))

'''
@csrf_exempt
def Webhook(request):
    if request.method == 'POST':
        # print("Data received from Webhook is: ", request.body)

        test = request.body.decode('utf-8')
        test = json.loads(test)

        for element in test['entry']:
            Test.objects.create(name="test", get_from_facebook=element['id'])
        return HttpResponse(request.GET.get("hub.challenge"))
'''