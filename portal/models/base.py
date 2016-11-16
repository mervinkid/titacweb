import django
from django.db import models


class BaseManager(models.Manager):
    """
    根据django版本
    """

    def __init__(self):
        models.Manager.__init__(self)
        self.django_version = int((django.get_version().split('.'))[1])

    def query(self):
        if self.django_version >= 6:
            queryset = self.get_queryset()
        else:
            queryset = self.get_query_set()
        return queryset
