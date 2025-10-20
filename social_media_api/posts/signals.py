from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        actor = instance.author
        if post.author != actor:
            Notification.objects.create(
                recipient=post.author,
                actor=actor,
                verb='commented on your post',
                target_ct=ContentType.objects.get_for_model(post.__class__),
                target_id=post.id
            )
