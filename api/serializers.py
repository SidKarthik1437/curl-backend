from rest_framework.serializers import ModelSerializer
from .models import Script
from .models import File


class ScriptSerializer(ModelSerializer):
    class Meta:
        model = Script
        fields = '__all__'
        
class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
