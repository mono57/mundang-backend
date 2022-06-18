import re

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

def hex_color_code_validator(value):
    pattern = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

    if not re.match(pattern, value):
        raise ValidationError(
            _('%(value)s is not a valid Hex color'),
            params={'value': value},
        )
