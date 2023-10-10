from django.db import models

class todoapp_TodoListItem(models.Model):
    content = models.TextField()
