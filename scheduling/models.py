from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from django_extensions.db.fields import AutoSlugField, UUIDField
from localflavor.us.models import USStateField

from organization.models import Organization, Venue, Membership, Role
from payroll.models import Formula


class Dance(models.Model):
    organization = models.ForeignKey(Organization, related_name="dances")
    venue = models.ForeignKey(Venue, related_name="dances")

    uuid = models.CharField(max_length=200)

    auto_slug = AutoSlugField(populate_from=['day'])

    staff = models.ManyToManyField(User, through='Timeslot')

    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.IntegerField(blank=True, null=True)

    # Allow customization on a per-dance basis
    # i.e. if band night or special event
    price = models.IntegerField(blank=True, null=True)
    price_low = models.IntegerField(blank=True, null=True)
    price_high = models.IntegerField(blank=True, null=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    @property
    def date(self):
        return self.start.date()

    def __str__(self):
        return '%s on %s' % (self.venue.name, self.start.date().isoformat())


class Lesson(models.Model):
    organization = models.ForeignKey(Organization, related_name="lessons")
    venue = models.ForeignKey(Venue, blank=True, null=True, related_name="lessons")
    dance = models.ForeignKey(Dance, blank=True, null=True, related_name="lessons")

    uuid = models.CharField(max_length=200)

    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True)

    staff = models.ManyToManyField(User, through='Timeslot')

    #lesson_template = models.ForeignKey('registration.models.LessonTemplate?')

    street1 = models.CharField(max_length=200, blank=True)
    street2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = USStateField(blank=True)
    zip_code = models.CharField(max_length=10, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField()


class Timeslot(models.Model):
    dance = models.ForeignKey(Dance, blank=True, null=True)
    lesson = models.ForeignKey(Lesson, blank=True, null=True)

    person = models.ForeignKey(User)
    role = models.ForeignKey(Role)

    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)

    notes = models.TextField(blank=True)

    formula = models.OneToOneField(Formula, blank=True, null=True)

    def get_proper_formula(self):
        if self.formula:
            return self.formula

        if self.dance:
            org_membership = Membership.objects.filter(person=self.person, organization=self.dance.organization, role=self.role).first()
            venue_membership = Membership.objects.filter(person=self.person, venue=self.dance.venue, role=self.role).first()
        elif self.lesson:
            org_membership = Membership.objects.filter(person=self.person, organization=self.lesson.organization, role=self.role).first()
            venue_membership = Membership.objects.filter(person=self.person, venue=self.lesson.venue, role=self.role).first()
        else:
            return self.role.formula

        if org_membership and org_membership.formula:
            return org_membership.formula
        if venue_membership and venue_membership.formula:
            return venue_membership.formula

        return self.role.formula

    @property
    def duration(self):
        return (self.end - self.start).total_seconds() / 60.0 / 60.0

admin.site.register(Dance)
admin.site.register(Lesson)
admin.site.register(Role)
admin.site.register(Timeslot)
