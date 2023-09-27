from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    super_todo = models.ForeignKey("Todo", on_delete=models.CASCADE, related_name="todos", blank=True, null=True)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

