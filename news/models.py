from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

# Create your models here.
class NewsType(models.Model):
    type = models.CharField(max_length=10,unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.type
    def get_topics_count(self):
        return NewsTopic.objects.filter(type=self).count()

class NewsTopic(models.Model):
    description = models.TextField()
    type = models.ForeignKey(NewsType,related_name='news_topic',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.type)
    def get_posts_count(self):
        return posts.objects.filter(topic=self).count()
    def get_last_post(self):
        return posts.objects.filter(topic=self).order_by('-created_date').first()
class posts(models.Model):
    message = models.TextField(max_length=450)
    topic = models.ForeignKey(NewsTopic,related_name='post_topic',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='created_by',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(null=True)
    def __str__(self):
        truncated_msg = Truncator(self.message)
        return truncated_msg.chars(30)