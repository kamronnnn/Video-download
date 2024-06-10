from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.


class Video(models.Model):
    name = models.CharField(max_length=50)
    video = models.FileField(upload_to='video/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'WMV'])
    ])

    def __str__(self):
        return self.name
