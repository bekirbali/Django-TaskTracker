from django.db import models

# Create your models here.

class Todo(models.Model):

    PRIORITY = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    )

    title = models.CharField(max_length=128)
    task = models.TextField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY, default=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} {self.is_done}'