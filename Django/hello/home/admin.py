from django.contrib import admin

from home.models import Contactus

# Here "home" humari app ka naam uske andar se humne Contacts ko import krdiya hai

admin.site.register(Contactus) #yeh line manually likhna hai

# Register your models here.
