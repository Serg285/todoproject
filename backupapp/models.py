from django.db import models

class backup(models.Model):
    backup_status = models.TextField()
    system_name = models.TextField()
    request_d = models.TextField()
    backup_type = models.TextField()
