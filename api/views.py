from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Script
from .serializers import ScriptSerializer
from .execution import execute
# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/scripts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of scripts'
        },
        {
            'Endpoint': '/scripts/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single script object'
        },
        {
            'Endpoint': '/scripts/create/',
            'method': 'POST',
            'body': {'body': {}},
            'description': 'Creates new script with data sent in post request'
        },
        {
            'Endpoint': '/scripts/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing script with data sent in post request'
        },
        {
            'Endpoint': '/scripts/id/execute/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a script'
        },
        {
            'Endpoint': '/scripts/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting script'
        },
    ]

    return Response(routes)


@api_view(['GET'])
def getScripts(request):
    scripts = Script.objects.all().order_by('-updated')
    serializer = ScriptSerializer(scripts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getScript(request, pk):
    scripts = Script.objects.get(id=pk)
    serializer = ScriptSerializer(scripts, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createScript(request):
    data = request.data
    script = Script.objects.create(
        body=data
    )
    serializer = ScriptSerializer(script, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
def updateScript(request, pk):
    data = request.data
    script = Script.objects.get(id=pk)
    serializer = ScriptSerializer(instance=script, data=data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteScript(request, pk):
    script = Script.objects.get(id=pk)
    script.delete()
    return Response('Script was deleted!')


@api_view(['GET'])
def executeScript(request, pk):
    scripts = Script.objects.get(id=pk)
    serializer = ScriptSerializer(scripts, many=False)
    
    execute(serializer.data)
    
    return Response(serializer.data)