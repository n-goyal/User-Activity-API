from rest_framework import serializers
from userActivityRestApi.models import User, ActivityPeriod


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ActivityPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = (
            'start_time',
            'end_time'
        )
