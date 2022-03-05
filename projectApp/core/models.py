from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProjectList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)  # <--- added
    name = models.CharField(max_length=200)
    shareduser = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Tabs(models.Model):
    projectList = models.ForeignKey(ProjectList, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Item(models.Model):
    tab = models.ForeignKey(Tabs, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()
    due_date = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.text
