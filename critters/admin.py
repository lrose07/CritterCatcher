from django.contrib import admin
from .models import Critter,\
    CritterType, CritterMonthHemisphereRelationship, CritterTimeRelationship,\
    Hour, Location, Month, Hemisphere

# Register your models here.
admin.site.register(Critter)
admin.site.register(CritterType)
admin.site.register(CritterTimeRelationship)
admin.site.register(CritterMonthHemisphereRelationship)
admin.site.register(Hour)
admin.site.register(Location)
admin.site.register(Month)
admin.site.register(Hemisphere)
