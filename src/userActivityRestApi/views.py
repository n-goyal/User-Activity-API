from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework import status

from userActivityRestApi.models import User, ActivityPeriod
from userActivityRestApi.serializers import UserSerializer, ActivityPeriodSerializer

from rest_framework.decorators import api_view


@api_view(['GET'])
def userList(request):
    print('hitting views')

    if request.method == 'GET':

        users = User.objects.all()
        userSerializer = UserSerializer(users, many=True)
        usersJson = userSerializer.data
        print(type(usersJson))

        for user in usersJson:
            activity = ActivityPeriod.objects.filter(
                user=User.objects.get(id=user.get('id'))
            )
            activitySerializer = ActivityPeriodSerializer(activity, many=True)

            user['activity_periods'] = activitySerializer.data

        return JsonResponse(usersJson, safe=False, status=status.HTTP_200_OK)
