# from django.http import JsonResponse
import api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from api import serializers

@api_view (['GET'])
def getRoutes (request):
    routes = [
        {
            'Endpoints' : '/start',
            'method': 'GET',
            'body': None,
            'description': 'Welcome page'
        },
        {
            'Endpoints' : '/signup',
            'method': 'POST',
            'body': {"body": ""},
            'description': 'SignupPage'
        },
        {
            'Endpoints' : '/login',
            'method': 'POST',
            'body': {"body": ""},
            'description': 'Login'
        },        
        {
            'Endpoints' : '/homepage',
            'method': 'GET',
            'body': None,
            'description': 'Homepage'
        },
        {
            'Endpoints' : '/bot',
            'method': 'GET',
            'body': None,
            'description': 'ChatBot'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getUser (request):
    users_data = User.objects.all()
    serializer = UserSerializer (users_data, many=True)
    return Response (serializer.data)

@api_view(['GET'])
def getUserData (request, pk):
    users_data = User.objects.get(user_email=pk)
    serializer = UserSerializer (users_data, many=False)
    return Response (serializer.data)


@api_view(['POST'])
def addUser (request):
    data = request.data

    newuser = User.objects.create (
        name = data['name'],
        user_email = data['user_email'],
        user_password = data['user_password']
    )

    serializer = UserSerializer (newuser, many=False)
    return Response (serializer.data)

@api_view(['PUT'])
def updateUser (request, pk):
    data = request.data

    newdata = User.objects.get (id=pk)

    serializer = UserSerializer (newdata, data=request.data)
    if serializer.is_valid ():
        serializer.save()
    return Response (serializer.data)


@api_view(['GET'])
def getReminder (request):
    reminders = Reminder.objects.all
    serializer = ReminderSerializer (reminders, many=True)
    return Response (serializer.data)


@api_view(['POST'])
def createReminder (request):
    data = request.data

    reminder = Reminder.objects.create (
        remind_date = data['remind_date'],
        reminder_description = data['reminder_description']
    )

    serializer = ReminderSerializer (reminder, many=False)
    return Response (serializer.data)

@api_view(['PUT'])
def updateReminder (request, pk):
    data = request.data

    reminder = Reminder.objects.get (id=pk)

    serializer = ReminderSerializer (reminder, data=request.data)
    if serializer.is_valid ():
        serializer.save()
    return Response (serializer.data)


@api_view(['DELETE'])
def deleteReminder (request, pk):
    reminder = Reminder.objects.get (id=pk)
    reminder.delete()
    return Response ('Reminder deleted!')