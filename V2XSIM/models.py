from django.db import models

class Scene(models.Model):

    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Test(models.Model):

    scene = models.ForeignKey(Scene, on_delete=models.PROTECT)
    status = models.IntegerField()

class Node(models.Model):

    name = models.CharField(max_length=200)
    node_type = models.IntegerField()

    def __str__(self):
        return 'Node %s' % self.name

class SceneConfig(models.Model):

    scene = models.ForeignKey(Scene, on_delete=models.CASCADE)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)

class V2XMessage(models.Model):

    info = models.CharField(max_length=500)

class MessageLog(models.Model):

    message_type = models.IntegerField()
    message = models.ForeignKey(V2XMessage, on_delete=models.PROTECT)
    node = models.ForeignKey(Node, on_delete=models.PROTECT)
    time = models.DateField()
