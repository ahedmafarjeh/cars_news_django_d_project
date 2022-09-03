from django.contrib import admin
from .models import NewsTopic,NewsType
# Register your models here.
admin.site.register(NewsType)
admin.site.register(NewsTopic)