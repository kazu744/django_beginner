from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=10)

    def __str__(self):
        return self.title