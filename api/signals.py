from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Vote

@receiver([post_save, post_delete], sender=Vote)
def update_post_vote_count(sender, instance, **kwargs):
    post = instance.post

    like_count = post.votes.filter(type='like').count()
    dislike_count = post.votes.filter(type='dislike').count()

    post.vote_count = like_count - dislike_count
    post.save(update_fields=['vote_count'])