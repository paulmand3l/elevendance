import json

from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from scheduling.models import Dance, Lesson, Timeslot



def send_money(request):
    person = User.objects.get(id=request.GET['id'])
    amount = request.GET['amount']
    # mandrill.send(person.email, amount, cc="cash@square.com")

def close_out(request):
    payroll = []
    kind = request.GET['kind'].lower()

    staffable = get_object_or_404({'dance': Dance, 'lesson': Lesson}[kind],
                                  id=request.GET['id'])

    for person in staffable.staff.distinct():
        if kind == 'dance':
            timeslots = list(Timeslot.objects.filter(person=person, dance=staffable))
            for lesson in staffable.lessons.all():
                timeslots += Timeslot.objects.filter(person=person, lesson=lesson)
        elif kind == 'lesson':
            timeslots = Timeslot.objects.filter(person=person, lesson=staffable)

        jobs = []
        total = 0
        for timeslot in timeslots:
            formula = timeslot.get_proper_formula()
            pay = formula.compute(heads=staffable.attendees.count(), duration=timeslot.duration)
            total += pay
            jobs.append( (timeslot.role.name, str(formula), pay) )

        payroll.append({
            'person': (person.get_full_name(), person.id),
            'jobs': jobs,
            'total': total,
        })

    return HttpResponse(json.dumps(payroll), content_type="application/json")
