from django.db import models

from account.models import Account

# Create your models here.
class LeaveRequest(models.Model):
    user = models.ForeignKey(Account, on_delete = models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField(max_length = 255)
    status = models.CharField(max_length = 30, default = 'Pending')
