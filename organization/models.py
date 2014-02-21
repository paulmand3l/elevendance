import recurrence.fields

from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField
from localflavor.us.models import USStateField


class Organization(models.Model):
    name = models.CharField(max_length=200)
    auto_slug = AutoSlugField(populate_from='name')

    founded = models.DateField('date organization was founded', blank=True, null=True)

    members = models.ManyToManyField(User, through='Membership')

    def isMember(self, person):
        return self.members.filter(person=person).exists()

    def __str__(self):
        return self.name


class Venue(models.Model):
    organization = models.ForeignKey(Organization, related_name="venues")

    name = models.CharField(max_length=200)
    auto_slug = AutoSlugField(populate_from='name')

    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.IntegerField(blank=True)

    # Used when automatically generating Dance objects
    default_price = models.IntegerField(blank=True, null=True)
    default_price_low = models.IntegerField(blank=True, null=True)
    default_price_high = models.IntegerField(blank=True, null=True)

    default_start = models.TimeField(blank=True, null=True)
    default_end = models.TimeField(blank=True, null=True)

    recurrence_type = recurrence.fields.RecurrenceField()

    members = models.ManyToManyField(User, through='Membership')

    def isMember(self, person):
        return (self.members.filter(person=person).exists() or
               self.organization.members.filter(person=person).exists())

    def __str__(self):
        return self.name


class Membership(models.Model):
    organization = models.ForeignKey(Organization, blank=True, null=True)
    venue = models.ForeignKey(Venue, blank=True, null=True)

    person = models.ForeignKey(User, related_name="memberships")

    role = models.CharField(max_length=100)


    notes = models.TextField(blank=True)


admin.site.register(Organization)
admin.site.register(Venue)
admin.site.register(Membership)
