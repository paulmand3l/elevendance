import recurrence.fields

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from django_extensions.db import fields


class Organization(models.Model):
    name = models.CharField(max_length=200)
    auto_slug = fields.AutoSlugField(populate_from='name')

    founded = models.DateField('date organization was founded', blank=True, null=True)

class Venue(models.Model):
    name = models.CharField(max_length=200)
    auto_slug = fields.AutoSlugField(populate_from='name')

    organization = models.ForeignKey(Organization, related_name="venues")

    # Used when automatically generating Dance objects
    default_price = models.IntegerField(blank=True, null=True)
    default_price_low = models.IntegerField(blank=True, null=True)
    default_price_high = models.IntegerField(blank=True, null=True)

    default_start = models.TimeField(blank=True, null=True)
    default_end = models.TimeField(blank=True, null=True)

    recurrence_type = recurrence.fields.RecurrenceField()

class Dance(models.Model):
    venue = models.ForeignKey(Venue, related_name="dances")
    organization = models.ForeignKey(Organization, related_name="dances")

    auto_slug = fields.AutoSlugField(populate_from=['venue', 'start'])

    # Allow customization on a per-dance basis
    # i.e. if band night or special event
    price = models.IntegerField(blank=True, null=True)
    price_low = models.IntegerField(blank=True, null=True)
    price_high = models.IntegerField(blank=True, null=True)

    start = models.DateTimeField()
    end = models.DateTimeField()
    #######

class RoleType(models.Model):
    name = models.CharField(max_length=100)

class Role(models.Model):
    dance = models.ForeignKey(Dance, blank=True, null=True, related_name="staff")
    venue = models.ForeignKey(Venue, blank=True, null=True, related_name="staff")
    organization = models.ForeignKey(Organization, blank=True, null=True, related_name="staff")

    user = models.ForeignKey(User, related_name="roles")

    role_type = models.ForeignKey(RoleType, related_name="roles")


admin.site.register(Organization)
admin.site.register(Venue)
admin.site.register(Dance)
admin.site.register(RoleType)
admin.site.register(Role)
