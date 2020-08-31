import functools
import logging

from django.db import transaction


logger = logging.getLogger(__name__)


def base_view(fn):
    """Decorator for all views"""
    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return logger.error(str(e))

    return inner
