from teams.models import team
from rest_framework import serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = ['id', 'teamname', 'description', 'creationtime', 'admin', 'members']

class TeamGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = ['teamname', 'description', 'creationtime', 'admin']

class TeamPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = team
        fields = ['id', 'teamname', 'description', 'creationtime', 'admin']