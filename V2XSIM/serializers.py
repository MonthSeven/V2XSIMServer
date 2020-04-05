from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Scene, Test, SceneConfig, Node, V2XMessage, MessageLog

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class SceneSerializer(serializers.ModelSerializer):
    class Mate:
        model = Scene
        fields = ('name', 'image', 'description')

class TestSerializer(serializers.ModelSerializer):
    class Mate:
        model = Test
        fields = ('scene', 'status')

class NodeSerializer(serializers.ModelSerializer):
    class Mate:
        model = Node
        fields = ('name', 'node_type')

class SceneConfigSerializer(serializers.ModelSerializer):
    class Mate:
        model = SceneConfig
        fields = ('scene', 'node')

class V2XMessageSerializer(serializers.ModelSerializer):
    class Mate:
        model = V2XMessage
        fields = ('info', )

class MessageLogSerializer(serializers.ModelSerializer):
    class Mate:
        model = MessageLog
        fields = ('message_type', 'message', 'node', 'time')
