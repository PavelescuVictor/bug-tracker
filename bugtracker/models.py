from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify

class Bug(models.Model):

    status_choices = (
        ('resolved','resolved'),
        ('unresolved', 'unresolved')
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=status_choices, default='unresolved')
    description = models.TextField()
    register_date = models.DateTimeField(default=timezone.now)
    solved_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bug-detail', kwargs={'pk': self.pk})
