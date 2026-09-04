from rest_framework import serializers
from tasks.models import Task

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields ="__all__"

            
    