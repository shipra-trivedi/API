from rest_framework import serializers
from .models import language

class languageSerializer(serializers.ModelSerializer):

    class Meta:
        model=language
        fields='__all__'