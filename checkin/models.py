from django.db import models
from django.contrib.auth.models import User

from organization.models import Organization, Venue
from scheduling.models import Dance, Lesson

class Attendance(models.Model):
  organization = models.ForeignKey(Organization)
  venue = models.ForeignKey(Venue, blank=True, null=True, related_name="attendees")
  dance = models.ForeignKey(Dance, blank=True, null=True, related_name="attendees")
  lesson = models.ForeignKey(Lesson, blank=True, null=True, related_name="attendees")

  person = models.ForeignKey(User)

  comp = models.BooleanField(default=False)
  paid = models.IntegerField()

  notes = models.TextField(blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
