from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from .models import News


@receiver(post_save, sender=News)
def clear_home_cache(sender, **kwargs):
    cache.clear()