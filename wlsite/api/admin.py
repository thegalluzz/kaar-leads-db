from django.contrib import admin
from .models import *

admin.site.register(ContactForm)
admin.site.register(LeadAds)
admin.site.register(LeadWebsite)
admin.site.register(LeadBackup)
admin.site.register(LogLead)