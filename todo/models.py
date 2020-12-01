from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date']
