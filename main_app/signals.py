from django.dispatch import receiver
from django.db import models
from django.contrib.auth import get_user_model
from .models import Profile

@receiver(models.signals.post_save, sender=get_user_model())
def create_student_after_user_init(sender, instance, created, **kwargs):
    if created:
        # logic runs after user creation (not update)
        Profile._default_manager.create(user=instance)