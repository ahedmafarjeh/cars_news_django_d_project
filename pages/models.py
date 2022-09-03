from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.
class CarType(models.Model):
    car_name = models.CharField(max_length=50)
    car_model = models.IntegerField(max_length=4)
    def __str__(self):
        return self.car_name

class Piece(models.Model):
    piece_name = models.CharField(max_length=200)
    car = models.ForeignKey(CarType,related_name='topics',on_delete=models.CASCADE)
    price = models.IntegerField(max_length=3)
    is_available = models.BooleanField()
    def __str__(self):
        return self.piece_name
    def get_posts_count(self):
        return posts.objects.filter(topic=self).count()
    def get_last_post(self):
        return posts.objects.filter(topic=self).order_by('-created_date').first()
class posts(models.Model):
    message = models.TextField(max_length=450)
    topic = models.ForeignKey(Piece,related_name='piece_topic',on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,related_name='p_created_by',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    truncator_msg = Truncator(message)
    def __str__(self):
        truncated_msg = Truncator(self.message)
        return self.truncated_msg.chars(30)