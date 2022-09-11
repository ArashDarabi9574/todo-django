from rest_framework import serializers
from todo.models import Task
from accounts.models import Profile

class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()
    class Meta:

        model = Task
        fields = "__all__"


    def get_absolute_url(self,obj):
          request = self.context.get('request')
          return request.build_absolute_uri(obj.pk)
    