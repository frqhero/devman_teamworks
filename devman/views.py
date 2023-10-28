from django.contrib import messages
from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.urls import reverse


def ask_students_choose_time(request):
    call_command('ask_students_choose_time')

    messages.success(
        request,
        (
            'Система прошла циклом по студентам и отправила просьбу указать'
            ' временные возможности тем, у кого указан ChatID.'
        ),
    )
    return HttpResponseRedirect(reverse('admin:devman_student_changelist'))
