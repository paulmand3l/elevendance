from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField
from localflavor.us.models import USStateField

from organization.models import Organization, Venue


class Dance(models.Model):
    organization = models.ForeignKey(Organization, related_name="dances")
    venue = models.ForeignKey(Venue, related_name="dances")

    auto_slug = AutoSlugField(populate_from=['day'])

    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.IntegerField(blank=True)

    # Allow customization on a per-dance basis
    # i.e. if band night or special event
    price = models.IntegerField(blank=True, null=True)
    price_low = models.IntegerField(blank=True, null=True)
    price_high = models.IntegerField(blank=True, null=True)

    day = models.DateField()
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return '%s on %s' % (self.venue.name, self.start.date().isoformat())


class Lesson(models.Model):
    organization = models.ForeignKey(Organization)
    venue = models.ForeignKey(Venue, blank=True, null=True)
    dance = models.ForeignKey(Dance, blank=True, null=True)

    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True)

    #lesson_template = models.ForeignKey('registration.models.LessonTemplate?')

    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField()


class Role(models.Model):
    organization = models.ForeignKey(Organization, blank=True, null=True)
    venue = models.ForeignKey(Venue, blank=True, null=True)

    name = models.CharField(max_length=100)
    admin = models.BooleanField(default=False)


class Timeslot(models.Model):
    dance = models.ForeignKey(Dance, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, blank=True, null=True)

    person = models.ForeignKey(User)
    role = models.ForeignKey(Role)

    start = models.DateTimeField()
    end = models.DateTimeField()

    notes = models.TextField(blank=True)


admin.site.register(Dance)
admin.site.register(Lesson)
admin.site.register(Role)
admin.site.register(Timeslot)
