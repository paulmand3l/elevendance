from django.db import models
from django.contrib import admin

class Formula(models.Model):
    KIND_CHOICES = (
        ('FLAT', 'Flat'),
        ('PER', 'Per hour or per head'),
        ('CUST', 'Custom')
    )

    kind = models.CharField(choices=KIND_CHOICES, default="PER", max_length=100)

    # Convenience fields for most common ways of paying people:
    # Flat rate, by hour or by person walking through the door
    flat = models.IntegerField('flat pay rate', blank=True, null=True)
    per_hour = models.IntegerField('hourly pay rate', blank=True, null=True)
    per_head = models.IntegerField('dollars per attendee', blank=True, null=True)

    # More convenience fields for slightly more complex formulas
    after_heads = models.IntegerField("only start counting attendees after this many", default=0)
    pay_cap = models.IntegerField("the max amount they can make", default=100000)

    # For seriously complex formulas, custom formulas are enabled
    #formula = models.TextField(blank=True, null=True)

    def compute(self, heads, duration):
        result = 0
        if self.per_hour:
            result += self.per_hour * duration

        if self.per_head:
            result += self.per_head * max(heads - self.after_heads, 0)

        if self.pay_cap:
            result = min(self.pay_cap, result)

        return result

    def __str__(self):
        output = []
        if self.per_hour:
            output.append('$%s/hr' % self.per_hour)

        if self.per_head:
            heads = '$%s/head' % self.per_head
            if self.after_heads != 0:
                heads += ' after %s' % self.after_heads
            output.append(heads)

        output = ' + '.join(output)

        if self.pay_cap != 100000:
            output += ' up to %s' % self.pay_cap

        return output

admin.site.register(Formula)
