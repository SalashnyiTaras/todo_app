""" Module models.py defines a model Task for this project

To create a model/SQL-table for current project class Task have been created inheriting from models.Model.
Created model has following fields: title, description, author, responsible, image, created, updated, completed.
It is also necessary to import User model from django.contrib.auth.models when defining model's fields.

For Task model there have been also added such features as object representation(model's title is used), image resizing,
and ordering. To resize images uploaded by user library PIL has been used.
"""

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Task(models.Model):
    """ A class which defines model fields its characteristics and methods of this model

    Attributes
    ----------
    title : CharField
        a title of model's object, max. 200 characters
    description : TextField
        a description of model's object, can be blank or null
    author : ForeignKey relationship with model User
        an author of model's object, can be blank or null, related_name='author'
    responsible : ManyToManyField relationship with model User
        people in charge of completing task, can be blank but can not be null, related_name='responsible'
    image : ImageField
        an image added by user when creating model's object, can be blank or null, will be uploaded to dir user_files
    created : DateTimeField
        date and time when model's object has been created
    updated : DateTimeField
        date and time when model's object has been last time updated
    completed : BooleanField
        shown if task have been completed or no, default = false

    Methods
    -------
    __str__()
        when object will be called, object's title will be returned
    save()
        function which redefines class save() in order to compresses an image uploaded by user
    class Meta:
        setting ordering that 'completed' items will be shown in the bottom
    """

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='author')
    responsible = models.ManyToManyField(User, blank=True, related_name='responsible')
    image = models.ImageField(null=True, blank=True, upload_to='user_files')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        """ makes a representation of class object - when object will be called, object's title  will be returned"""

        return self.title

    def save(self, *args, **kwargs):
        """ function which redefines class' save() in order to compresses an image uploaded by user.
        Important: resizing function can cause problems during deployment. It can be a good idea to remove it.

        Parameters:
        -----------
        *args
            arguments that class can take if necessary
        **kwargs
            keyword-arguments that class can take if necessary
        """

        super(Task, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        """ class Meta is applied to the Task model setting that 'completed' items will be shown in the bottom

        Attributes
        ----------
        ordering : list
            defines how items will be ordered
        """

        ordering = ['completed']
