from __future__ import unicode_literals

from django.db import models
from jsonfield import JSONField


class Flat(models.Model):
    data = JSONField()
