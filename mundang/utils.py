from django.db import models
from django.urls import reverse
from django.http import QueryDict

class TimestampModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def reverse_query_string(viewname, params):
    q = QueryDict('', mutable=True)
    q.update(params)

    reverse_url = reverse(viewname) + q.urlencode()

    return reverse_url
