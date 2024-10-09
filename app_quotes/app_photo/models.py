from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


def validate_file_size(value):
    file_size = value.size

    if file_size > settings.MAX_FILE_SIZE:
        raise ValidationError('Max file size 1Mb')
    return value


# Create your models here.
class Pictures(models.Model):
    description = models.CharField(max_length=300)
    path = models.ImageField(upload_to='images', validators=[validate_file_size])
