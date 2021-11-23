from rest_framework.serializers import ModelSerializer

from .models import Reminder, User

class UserSerializer (ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReminderSerializer (ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'