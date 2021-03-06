from django.db import models


#ACL type approach
# 0  = anonymous
# 10 = high privacy
# 20 = default - high privacy w/ med group privacy
# 2X = group privacy range
# 40 = PUBLIC

PRIVACY_LEVEL = (
    (0, 'Hidden'),
    (10, 'High Privacy'),
    (20, 'Medium Privacy'),
    (30, 'Low Privacy'),
    (40, 'Highly Public'),
)

PRIVACY_LEVEL_SIMPLE = (
    (0, 'Hidden'),
    (40, 'Public'),
)


class Privacy(models.Model):
    privacy = models.IntegerField(max_length=5, choices=PRIVACY_LEVEL,
                                  default=20, blank=True, null=True)

    class Meta:
        abstract = True
