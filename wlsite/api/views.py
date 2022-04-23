from lib2to3.pgen2 import token
from urllib.request import HTTPPasswordMgrWithDefaultRealm
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authtoken.models import Token

from django.conf import settings

from .serializers import ContactFormSerializer, LeadAdsSerializer
from .models import LeadAds, LeadBackup, LeadWebsite, LeadMSN, LogLead
import json


#Homepage
def Home(request):
    if request.method == 'GET':
        return HttpResponse(f'<p>Kaar!<p>')

#Send a Contact Form
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

#List all Leads, or create a new Lead.

class LeadAdsAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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

#Facebook Webhook
@csrf_exempt
def WebhookAds(request):

    if request.method == 'GET':
        return HttpResponse(request.GET.get("hub.challenge"))

    if request.method == 'POST':
        payload_raw = request.body.decode('utf-8')
        payload = json.loads(payload_raw)

        try:
            LeadBackup.objects.create(
                leadbackup_date = datetime.now(),
                leadbackup_backup = payload_raw,
                )
        except Exception as e:
            print(repr(e))
            LogLead.objects.create(
                log_date = datetime.now(),
                exeption_origin = "first try except of WebhookAds",
                log_exeption = str(repr(e)),
                )
        try:
            LeadAds.objects.create(
                lead_id = payload['entry'][0]['changes'][0]['value']['leadgen_id'],
                created_time = payload['entry'][0]['changes'][0]['value']['created_time'],
                ad_id = payload['entry'][0]['changes'][0]['value']['ad_id'],
                ad_name = 'ad_name',
                adset_id = 'adset_id',
                adset_name = 'adset_name',
                campaign_id = 'campaign_id',
                campaign_name = 'campaign_name',
                form_id = payload['entry'][0]['changes'][0]['value']['form_id'],
                full_name = 'full_name',
                phone_number = 'phone_number',
                email = 'email',
                car_request = 'adgroup_name',
                )
        except Exception as e:
            print(repr(e))
            LogLead.objects.create(
                log_date = datetime.now(),
                exeption_origin = "second try except of WebhookAds",
                log_exeption = str(repr(e)),
                )
        return HttpResponse(request.GET.get("hub.challenge"))
    else:
        return Response(status.HTTP_400_BAD_REQUEST)

#Website Webhook
@csrf_exempt
def WebhookWebsite(request):

    if request.method == 'GET':
        return HttpResponse(f'Kaar')

    if request.method == 'POST':
        payload = request.body.decode('utf-8')
        payload = json.loads(payload)

        try:
            LeadBackup.objects.create(
                leadbackup_date = datetime.now(),
                leadbackup_backup = payload,
                )
        except Exception as e:
            print(repr(e))
            LogLead.objects.create(
                log_date = datetime.now(),
                exeption_origin = "first try except of WebhookAds",
                log_exeption = str(repr(e)),
                )
        try:
            LeadWebsite.objects.create(
                created_time = datetime.datetime.now(),
                full_name = 'Full Name',
                phone_number = 'Phone Number',
                email = 'email',
                car_request = 'car request',
                )
        except Exception as e:
            print(repr(e))
            LogLead.objects.create(
                log_date = datetime.now(),
                exeption_origin = "first try except of WebhookAds",
                log_exeption = str(repr(e)),
                )
        return HttpResponse(request.GET.get("hub.challenge"))
    else:
        return Response(status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def WebhookMSN(request):

    if request.method == 'GET':
        return HttpResponse(f'Kaar')

    if request.method == 'POST':
        payload = request.body.decode('utf-8')
        payload = json.loads(payload)

        try:                
            LeadBackup.objects.create(
                leadbackup_date = datetime.now(),
                leadbackup_backup = payload,
                )
        except Exception as e:
            print(repr(e))
            LogLead.objects.create(
                log_date = datetime.now(),
                exeption_origin = "first try except of WebhookAds",
                log_exeption = str(repr(e)),
                )
        try:
            LeadMSN.objects.create(
                created_time = datetime.datetime.now(),
                full_name = 'full_name',
                phone_number = 'phone_number',
                email = 'email',
                car_request = 'car_request', 
                )
        except Exception as e:
            print(repr(e))
            LogLead.objects.create(
                log_date = datetime.now(),
                exeption_origin = "first try except of WebhookAds",
                log_exeption = str(repr(e)),
                )
        return HttpResponse(request.GET.get("hub.challenge"))
    else:
        return Response(status.HTTP_400_BAD_REQUEST)