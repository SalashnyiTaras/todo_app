""" This modules is in charge of handling web requests and returning web responses represented in json.

The functionality of this module is based on functions which take web request. View-functions are decorated with
@api_view, being imported from rest_framework.decorators, which is used to allows/restricts HTTP methods which can be
used upon function.

In the body of function a query to data base of model Task is made. The QueryDict returned from data base will be
serialized and passed to Response (class imported from rest_framework.response). Response will be returned to client
as json.
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TaskSerializer
import base.models


@api_view(['GET'])
def api_overview(request):
    """ A function which takes web request and return json representation of possible API's endpoints.

    Decorators
    ----------
    api_view : list
        takes http methods which will be interpreted as allowed upon current function
    Parameters
    -----------
    request : object
        sent by client to trigger response from projects' API
    Returns
    -------
    Response
         json representation of possible API's endpoints
    """

    api_urls = {
        'List': '/task-list',
        'Detail View': '/task-details/<str:pk>',
    }

    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    """ A function which takes web request and return json representation of all objects of Task model.

    Decorators
    ----------
    api_view : list
        takes http methods which will be interpreted as allowed upon current function
    Parameters
    -----------
    request : object
        sent by client to trigger response from projects' API
    Returns
    -------
    Response
         json representation of all objects of Task model
    """

    tasks = base.models.Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def task_details(request, pk):
    """ A function which takes web request and return json representation of detailed info of object of Task model.

    Decorators
    ----------
    api_view : list
        takes http methods which will be interpreted as allowed upon current function
    Parameters
    -----------
    request : object
        sent by client to trigger response from projects' API
    pk : int
        primary key/id of a particular object of Task model
    Returns
    -------
    Response
         json representation of detailed info of an object of Task model
    """

    task = base.models.Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)
