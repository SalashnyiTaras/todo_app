""" Module serializers.py is in charge of converting objects of project's models into json type.

This module is based on use of serializers of django rest_framework to represent a state of models' object. To do so,
app class TaskSerializer created by inheriting from serializers.ModelSerializer. The model Task is imported from base
app and passed in TaskSerializer to be serialized.
"""

from rest_framework import serializers
import base.models


class TaskSerializer(serializers.ModelSerializer):
    """ A class which provides serialization of models' data. Class is inherited from serializers.ModelSerializer

    Attributes
    ----------
    model : object
        a model to be serialized
    fields : str/list
        fields of above specified model to be serialized
    """

    class Meta:
        model = base.models.Task
        fields = '__all__'
