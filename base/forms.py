""" Module forms.py make changes to User model and UserCreationForm

The idea behind this module is to make an email field of User model active - it should be filled during
registration and afterwards should be saved in data base. To do so, UserRegisterForm class will be created inheriting
from UserCreationForm(being imported from django.contrib.auth.forms).

Email field has been imported from django forms.

Last but not least, it is necessary to specify fields of User model which should be active. It is possible to do
using class Meta and when setting User as a model.
 """

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """ A class used to add email field to User model. Class inherits from UserCreationForm.

    Attributes:
    ----------
    model : class
        name of class to be changed
    fields : list
        field which should be active in model specified above
    email : class
        any type of email field
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
