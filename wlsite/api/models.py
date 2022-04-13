from django.db import models
from .constants import CATEGORY, STATUS

# Create your models here.

class ContactForm(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=25, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    details = models.CharField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'contact-form ' + self.first_name + ' ' + self.last_name + ' ' + str(self.date)

    class Meta:
        verbose_name_plural = "Contact Forms"

class LeadAds(models.Model):
    lead_id = models.CharField(max_length=250)
    # created_time = models.DateField(max_length=250)
    created_time = models.CharField(max_length=250)
    ad_id = models.CharField(max_length=250)
    ad_name = models.CharField(max_length=250)
    adset_id = models.CharField(max_length=250)
    adset_name = models.CharField(max_length=250)
    campaign_id = models.CharField(max_length=250)
    campaign_name = models.CharField(max_length=250)
    form_id = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=250)
    car_request = models.CharField(max_length=250)
    agent_id = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=CATEGORY, default='nuovo_lead') 
    status = models.CharField(max_length=250, choices=STATUS, default='da_richiamare')


    def __str__(self):
        return 'Lead Ad' + self.full_name + ' ' + str(self.created_time)

class LeadWebsite(models.Model):
    #created_time = models.DateTimeField(auto_now_add=True)
    created_time = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=250)
    car_request = models.CharField(max_length=250)
    agent_id = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=CATEGORY, default='nuovo_lead') 
    status = models.CharField(max_length=250, choices=STATUS, default='da_richiamare')

    def __str__(self):
        return 'Lead Website' + self.full_name + ' ' + str(self.created_time)

class LeadMSN(models.Model):
    #created_time = models.DateTimeField(auto_now_add=True)
    created_time = models.CharField(max_length=250)
    full_name = models.CharField(max_length=250, null=False, blank=False)
    phone_number = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=250)
    car_request = models.CharField(max_length=250)
    agent_id = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=CATEGORY, default='nuovo_lead') 
    status = models.CharField(max_length=250, choices=STATUS, default='da_richiamare')

    def __str__(self):
        return 'Lead Messenger' + self.full_name + ' ' + str(self.created_time)


class LeadBackup(models.Model):
    leadbackup_date = models.DateTimeField(auto_now_add=True)
    leadbackup_backup = models.TextField(max_length=2000)

    def __str__(self):
        return 'Lead Back Up' + ' ' + str(self.id) + ' ' + str(self.leadbackup_date)