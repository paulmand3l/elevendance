from django.db import models

from organization.models import Membership
from scheduling.models import Role, Timeslot

class Formula(models.Model):
  membership = models.ForeignKey(Membership, blank=True, null=True)
  role = models.ForeignKey(Role, blank=True, null=True)
  timeslot = models.ForeignKey(Timeslot, blank=True, null=True)

  # Convenience fields for most common ways of paying people:
  # By hour or by person walking through the door
  per_hour = models.IntegerField('hourly pay rate', blank=True, null=True)
  per_head = models.IntegerField('dollars per attendee', blank=True, null=True)

  # More convenience fields for slightly more complex formulas
  after_heads = models.IntegerField("only start counting attendees after this many", default=0)
  pay_cap = models.IntegerField("the max amount they can make", default=100000)
