from django.db import models
from django.utils import timezone
# from django.contrib.postgres.fields import ArrayField

# User model
class User(models.Model):
    # Name
    name = models.CharField(max_length=100, null=True, default='')
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'User'
