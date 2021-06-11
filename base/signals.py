""" Module signals.py makes possible for users to receive notification on email after a task has been assign to them.

Each time when instance of base.models.Task is created and the field responsible is not NUll and not Blank, users who
was marked as responsible will get email-notification. It is possible to create such functionality using
django.db.models.signals m2m_changed, which reacts after any modification of ManyToManyField responsible.

Task model will be a sender indicating changes in data base. Function responsible_changed becomes a receiver after
decorator @receiver was applied.

If receiver detects a signal function send_mail from django.core.mail will notify users in charge.
"""

from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.core.mail import send_mail
from base.models import Task


@receiver(m2m_changed, sender=Task.responsible.through)
def responsible_changed(sender, instance, **kwargs):
    """ A function which sends email notification to users when Task model field  - responsible is not empty.

    Decorators
    ----------
    receiver :
        takes signal - m2m_changed and sender of the signal - model name and through-attribute to access m2m field

    Parameters
    -----------
    instance : object
        any object of Task model created by user
    sender : class
        model class of ManyToManyField, which sends signals
    """

    emails = []
    for person in instance.responsible.all():
        emails.append(person.email)
    send_mail('Hello from Taras',
              f'Hello! {instance.author} just assigned a new task for you!'
              f' Check it out!:http://127.0.0.1:8000/task/{instance.id}',
              'benjamin.coinbull@gmail.com',
              emails,
              fail_silently=False)
