""" This modules is in charge of handling web requests and returning web responses.

The functionality of this module is based on class-based views which do a lot of logic behind the scene. Detailed info
about class-based views can be found here: https://docs.djangoproject.com/en/3.2/topics/class-based-views/

This modules provides logic for ListView, DetailView, CreateView, UpdateView, DeleteView, FormView.
Also, creation of registration and login views required importing LoginView from django.contrib.auth.views and
UserRegisterForm from base.forms.

Sometimes class-based view makes queries to data base calling Task model.

This module also defines features that restrict access to the website for unauthorized users. To do so,
LoginRequiredMixin should be pass to a view. Another restriction that has been implemented is that in order to modify
or delete task, user must be an author of the post.

Some helpers functions such reverse_lazy or redirect have been used in modules when working with templates.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from base.models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from base.forms import UserRegisterForm
from django.contrib.auth import login
from django.shortcuts import redirect


class TaskLoginView(LoginView):
    """ A class used to perform logic for creating login page. Class inherits from LoginView.

    Attributes
    ----------
    template_name : str
        name of template which should be populated with data and rendered afterwards
    fields : list
        field which should be active in model specified above
    redirect_authenticated_user : Boolean
        if the user is authenticated, user will redirected

    Methods
    -------
    get_success_url()
        defines a URL, where after successful login user will be redirected
    """

    template_name = 'base/task_login_view.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        """ defines a URL, where after successful login user will be redirected

        Returns
        -------
        reverse_lazy()
            function which will render template, which name is specified in brackets
        """

        return reverse_lazy('tasks')


class RegisterView(FormView):
    """ A class used to perform logic for creating register page. Class inherits from FormView.

    Attributes
    ----------
    template_name : str
        name of template which should be populated with data from the form and rendered by afterwards
    form_class : class
        form which will be populated with data entered by user
    success_url : func
        defines a URL, where after successful registration user will be redirected

    Methods
    -------
    form_valid()
        defines a URL, where after successful login user will be redirected
    get()
        defines a URL, where after successful login user will be redirected
    """

    template_name = 'base/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        """ checks if form was populated with correct data to register user

        Parameters
        ----------
        form : form
            form filled with user data

        Returns
        -------
        super()
            method used to redefine parent method
        """

        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        """ check if user is authenticated, if True - user will be redirected

        Returns
        -------
        redirect()
            URL of template where to send user
        super()
            method used to redefine parent method
        """

        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterView, self).get(*args, **kwargs)


class TaskListView(LoginRequiredMixin, ListView):
    """ A class used to perform logic for creating page where all model's object will be displayed.
    Class inherits from ListView and LoginRequiredMixin - used to enable only logged int user to see the page.

    Attributes
    ----------
    model : class
        models upon which query will be made
    context_object_name : str
        a name used for accessing data in templates
    template_name : html template
        name of template which should be populated with data and rendered
    """

    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task_list_view.html'


class TaskDetailView(LoginRequiredMixin, DetailView):
    """ A class used to perform logic for creating page where details about model's object will be displayed.
    Class inherits from DetailView and LoginRequiredMixin - used to enable only logged in user to see the page.

    Attributes
    ----------
    model : class
        models upon which query will be made
    context_object_name : str
        a name used for accessing data in templates
    template_name : html template
        name of template which should be populated with data and rendered
    """

    model = Task
    context_object_name = 'task'
    template_name = 'base/task_detail_view.html'


class TaskCreateView(LoginRequiredMixin, CreateView):
    """ A class used to perform logic for creating model's object. Class inherits from CreateView and
     LoginRequiredMixin - used to enable only logged in user to see the page.

    Attributes
    ----------
    model : class
        models upon which query will be made
    fields : str
        model's fields which can be populated with data when creating an object
    success_url : func
        defines a URL, where after successful creation of object user will be redirected
    template_name : html template
        name of template which should be populated with data and rendered

    Methods
    -------
    form_valid()
        A function that makes a user who is creating task to be an author of the task
    """

    model = Task
    fields = ['title', 'description', 'responsible', 'completed', 'image']
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_create_view.html'

    def form_valid(self, form):
        """ A function that makes a user who is creating task to be an author of the task

        Returns
        -------
        super()
            method used to redefine parent method
        """

        form.instance.author = self.request.user
        print(form.instance.author)
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ A class used to perform logic for creating model's object. Class inherits from CreateView and
     LoginRequiredMixin - used to enable only logged in user to see the page.

    Attributes
    ----------
    model : class
        models upon which query will be made
    fields : str
        model's fields which can be populated with data when creating an object
    success_url : func
        defines a URL, where after successful creation of object user will be redirected
    template_name : html template
        name of template which should be populated with data and rendered

    Methods
    -------
    form_valid()
        A function that makes a user who is creating task to be an author of the task
    test_func()
        A function that allows to modify model's object only being an author of the model's object
    """

    model = Task
    fields = ['title', 'description', 'responsible', 'completed', 'image']
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_create_view.html'

    def form_valid(self, form):
        """A function that makes a user who is updating task to be an author of the task

        Returns
        -------
        super()
            method used to redefine parent method
        """
        form.instance.author = self.request.user
        return super(TaskUpdateView, self).form_valid(form)

    def test_func(self):
        """ function that allows to modify model's object only being an author of the model's object """

        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A class used to perform logic for deleting model's object. Class inherits from DeleteView, UserPassesTestMixin,
     LoginRequiredMixin - used to enable only logged in user to see the page.

    Attributes
    ----------
    model : class
        models upon which query will be made
    fields : str
        model's fields which can be populated with data when creating an object
    success_url : func
        defines a URL, where after successful creation of object user will be redirected
    template_name : html template
        name of template which should be populated with data and rendered

    Methods
    -------
    test_func()
        A function that allows to modify model's object only being an author of the model's object
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'base/task_delete_view.html'

    def test_func(self):
        """ function that allows to modify model's object only being an author of the model's object """

        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False
