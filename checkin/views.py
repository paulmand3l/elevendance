import json

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from scheduling.models import Dance, Lesson, Timeslot
from checkin.models import Attendance



def checkin(request):
    name = request.GET['name']
    email = request.GET['email']
    kind = request.GET['kind']
    attendable = request.GET['attendable']

    get_filter = {}
    if name:
        person = get_filter['profile__name'] = name
    if email:
        person = get_filter['email'] = email

    person = User.objects.get_or_create(**get_filter)

    attendable = get_object_or_404({'dance': Dance, 'lesson': Lesson}[kind],
                                   id=attendable)

    args = {
        'organization': attendable.organization,
        'venue': attendable.venue,
        kind: attendable,
        'person': person,
        'paid': request.GET['paid'],
        'comp': request.GET['comp']
    }
