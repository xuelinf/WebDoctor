from __future__ import unicode_literals

from django.db import models

# create the file table
class file_zone(models.Model):
    userID = models.CharField(max_length=20)
    fileName = models.FileField(upload_to='./upload/')

    def __unicode__(self):
        return self.userID

