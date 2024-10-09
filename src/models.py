from django.db import models
from django.contrib.auth import get_user_model

class UserModel(models.Model):

    # RECIEVED="RECIEVED"
    # COMPLETED="COMPLETED"
    # INPROGRESS="IN-PROGRESS"
    # STATUS_CHOICES = [
    #     (RECIEVED, "RECIEVED"),
    #     (COMPLETED, "COMPLETED"),
    #     (INPROGRESS, "IN-PROGRESS"),
    # ]
    
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=False, null=False)
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False, null=False, default=RECIEVED)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.email} - {self.created_at}"
