from rest_framework import serializers
from .models import *

class ClassSerializer(models.Model):
    class Meta:
        model=Class
        fields = [
            'id',
            
        ]