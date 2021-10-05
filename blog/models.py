from django.db import models


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ":" + self.description

    class Meta:
        ordering = ['date_created']
