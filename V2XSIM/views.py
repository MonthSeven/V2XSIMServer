from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from .models import Scene, Test, SceneConfig, Node, V2XMessage, MessageLog
from .serializers import UserSerializer, GroupSerializer
from .serializers import SceneSerializer, SceneConfigSerializer, TestSerializer
from .serializers import NodeSerializer, V2XMessageSerializer, MessageLogSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class SceneViewSet(viewsets.ModelViewSet):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer

class SceneConfigViewSet(viewsets.ModelViewSet):
    queryset = SceneConfig.objects.all()
    serializer_class = SceneConfigSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

class V2XMessageViewSet(viewsets.ModelViewSet):
    queryset = V2XMessage.objects.all()
    serializer_class = V2XMessageSerializer

class MessageLogViewSet(viewsets.ModelViewSet):
    queryset = MessageLog.objects.all()
    serializer_class = MessageLogSerializer
