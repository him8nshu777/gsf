from django.db import models
from django.conf import settings
from accounts.models import Customer,Employee, UserProfile
from django.utils.timezone import now

class Chat(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(UserProfile, related_name='received_messages', null=True, blank=True, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"Message from {self.sender.user.username} to {self.receiver.user.username if self.receiver else 'employees'}"

    class Meta:
        ordering = ['time']
