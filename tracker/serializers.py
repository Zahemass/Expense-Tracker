from rest_framework import serializers
from .models import AddItems

class AddItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddItems
        fields = ('id','Purpose','Amount','Reason')