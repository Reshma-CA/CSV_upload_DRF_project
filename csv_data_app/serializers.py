from rest_framework import serializers
from .models import User

class User_Model_Serializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=True)  

    class Meta:
        model = User
        fields = ['name', 'email', 'age']


    def validate_name(self,value):
        if not value or not value.strip():  # Ensure name is non-empty
            raise serializers.ValidationError("Name must be a non-empty string.")
        return value



    def validate_age(self, value):
        if value <= 0 or value >= 120:  # Allow 0 and 120 as valid values
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return value
        
