from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True,
                            validators=[RegexValidator(
                                regex='^[a-z0-9]+(-[a-z0-9]+)*$'
                                )])

    content = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.slug} {self.title}"
