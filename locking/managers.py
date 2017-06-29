import datetime
import django

from django.db.models import Q, Manager
from django.utils import timezone

from locking import settings as locking_settings

def point_of_timeout():
    delta = datetime.timedelta(seconds=locking_settings.LOCK_TIMEOUT)
    return timezone.now() - delta


class LockedManager(Manager):

    def get_queryset(self):
        timeout = point_of_timeout()
        if django.VERSION < (1, 7):
            qs = super(LockedManager, self).get_query_set()
        else:
            qs = super(LockedManager, self).get_queryset()
        return qs.filter(_locked_at__gt=timeout, _locked_at__isnull=False)

    if django.VERSION < (1, 7):
        get_query_set = get_queryset


class UnlockedManager(Manager):

    def get_queryset(self):
        timeout = point_of_timeout()
        if django.VERSION < (1, 7):
            qs = super(UnlockedManager, self).get_query_set()
        else:
            qs = super(UnlockedManager, self).get_queryset()
        return qs.filter(Q(_locked_at__lte=timeout) | Q(_locked_at__isnull=True))

    if django.VERSION < (1, 7):
        get_query_set = get_queryset
