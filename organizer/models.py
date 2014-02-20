import recurrence.fields

from django.db import models

from django_extensions.db import fields


class Organization(models.Model):
    name = models.CharField(max_length=200)
    auto_slug = fields.AutoSlugField(populate_from='name')

    founded = models.DateField('date organization was founded')

class Venue(models.Model):
    name = models.CharField(max_length=200)
    auto_slug = fields.AutoSlugField(populate_from='name')

    organization = models.ForeignKey(Organization)

    # Used when automatically generating Dance objects
    default_price = models.IntegerField(blank=True, null=True)
    default_price_low = models.IntegerField(blank=True, null=True)
    default_price_high = models.IntegerField(blank=True, null=True)

    default_start = models.DateTimeField(blank=True, null=True)
    default_end = models.DateTimeField(blank=True, null=True)

    recurrence_type = recurrence.fields.RecurrenceField()

class Dance(models.Model):
    venue = models.ForeignKey(Venue)
    organization = models.ForeignKey(Organization)

    auto_slug = fields.AutoSlugField(populate_from=['venue', 'start'])

    # Allow customization on a per-dance basis
    # i.e. if band night or special event
    price = models.IntegerField(blank=True, null=True)
    price_low = models.IntegerField(blank=True, null=True)
    price_high = models.IntegerField(blank=True, null=True)

    start = models.DateTimeField()
    end = models.DateTimeField()
    #######
