from django.shortcuts import render

from django.http.response import JsonResponse
from django.http import HttpResponse
from rest_framework import status

from userActivityRestApi.models import User, ActivityPeriod
from userActivityRestApi.serializers import UserSerializer, ActivityPeriodSerializer

from rest_framework.decorators import api_view


@api_view(['GET'])
def getHomePage(request):
    return HttpResponse('<p><h2>Welcome to user activity data api</h2> <br /> Use <b>https://stark-escarpment-05147.herokuapp.com/api/v1/users to view all user data</b></p>')


@api_view(['GET'])
def userList(request):

    if request.method == 'GET':
        print('Fetching activity data from the user database...')
        try:
            users = User.objects.all()
            userSerializer = UserSerializer(users, many=True)
            usersJson = userSerializer.data
            print('Fetch completed!')
            print('Found {} records...'.format(len(usersJson)))
            if len(usersJson) == 0:
                # return no data found
                return JsonResponse(
                    {
                        'message': 'No user data found in the system',
                        'ok': 'true'
                    },
                    safe=False,
                    status=status.HTTP_204_NO_CONTENT
                )
            else:
                # success response
                for user in usersJson:
                    # get activity periods for the respective user
                    activity = ActivityPeriod.objects.filter(
                        user=User.objects.get(id=user.get('id'))
                    )
                    activitySerializer = ActivityPeriodSerializer(
                        activity, many=True)
                    user['activity_periods'] = activitySerializer.data
                    user['ok'] = 'true'
                return JsonResponse(
                    usersJson,
                    safe=False,
                    status=status.HTTP_200_OK
                )
        except:
            # Failure
            return JsonResponse(
                {
                    'message': 'Server failure, we\'ll be back soon :)!',
                    'ok': 'false'
                },
                safe=False,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# @api_view(['GET'])
# def getUser(request):
#     if request.Method == 'GET':
#         userId = request.get('id')
#         print('Fetching activity data for user {}...'.format(userId))
#         try:
#             # fetch user info
#             user = User.objects.get(id=userId)
#             userJson = UserSerializer(user).data
#             print('Found {} record...'.format(len(usersJson)))
#             if len(usersJson) == 0:  # return no data found
#                 return JsonResponse(
#                     {
#                         'message': 'No user found in the system, Please check the user Id and try again',
#                         'ok': 'true'
#                     },
#                     safe=False,
#                     status=status.HTTP_204_NO_CONTENT
#                 )
#             else:
#                 # fetch activity periods
#                 activity = ActivityPeriod.objects.filter(
#                     user=User.objects.get(id=userId)
#                 )
#                 activitySerializer = ActivityPeriodSerializer(
#                     activity, many=True
#                 )
#                 userJson['activity_periods'] = activitySerializer.data
#                 return JsonResponse(
#                     userJson,
#                     safe=False,
#                     status=status.HTTP_200_OK
#                 )
#         except:
#             # Failure
#             return JsonResponse(
#                 {
#                     'message': 'Server failure, we\'ll be back soon :)!',
#                     'ok': 'false'
#                 },
#                 safe=False,
#                 status=status.HTTP_200_OK,
#             )
