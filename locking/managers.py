from django.db.models import Q, Manager
from django.utils import timezone
from locking import settings as locking_settings

import datetime

"""
    LOCKED
            if (datetime.today() - self.locked_at).seconds < LOCK_TIMEOUT:


            self.locked_at < (NOW - TIMEOUT)
"""

def point_of_timeout():
    delta = datetime.timedelta(seconds=locking_settings.LOCK_TIMEOUT)
    return timezone.now() - delta

class LockedManager(Manager):
    def get_queryset(self):
        timeout = point_of_timeout()
        return super(LockedManager, self).get_query_set().filter(_locked_at__gt=timeout, _locked_at__isnull=False)

class UnlockedManager(Manager):
    def get_queryset(self):
        timeout = point_of_timeout()
        return super(UnlockedManager, self).get_query_set().filter(Q(_locked_at__lte=timeout) | Q(_locked_at__isnull=True))
