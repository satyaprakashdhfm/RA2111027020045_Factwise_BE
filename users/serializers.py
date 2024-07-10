from users.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'creation_time', 'user_description']

# Serializer tailored for GET requests to limit the fields shown
class UserGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'creation_time', 'user_description']

# Serializer designed for PATCH requests to prevent updating the username field
class UserPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'name', 'creation_time', 'user_description']
        read_only_fields = ['username']

