from django.db import models


def randomize_queryset(func):
    def wrap(self):
        queryset = func(self)
        return queryset.order_by('?')

    return wrap

class QuoteManager(models.Manager):
    @randomize_queryset
    def find_random_quotes(self):
        all = self.get_queryset()
        not_fetched_qs = all.filter(fetched=False)

        if all.exists() and not not_fetched_qs.exists():
            all.update(fetched = False )
            return all

        return not_fetched_qs