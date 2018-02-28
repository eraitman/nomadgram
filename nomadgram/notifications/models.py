from django.db import models
from nomadgram.users import models as user_models
from nomadgram.images import models as image_models

class Notification(image_models.TimeStampedModel):
    
    TYPE_CHOICES = (
        ('like', 'Like'),
        ('comment','Comment'),
        ('follow', 'Follow')
    )

    creator = models.ForeignKey(user_models.User, related_name='creator', on_delete=models.PROTECT)
    to = models.ForeignKey(user_models.User, related_name='to', on_delete=models.PROTECT)
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image, null=True, blank=True, on_delete=models.PROTECT)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return 'From {} to {}'.format(self.creator,self.to)
