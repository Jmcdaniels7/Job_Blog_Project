from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Post model
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Review model
class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.author} - {self.rating}'


#Jacob McDaniels, 10/11/2024, 7:08pm
