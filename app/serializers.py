from rest_framework import serializers
from app.models import Details,Actor

class DetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = "__all__"

class ActorSerializer(serializers.HyperlinkedModelSerializer):
    details = serializers.HyperlinkedRelatedField(many=True, read_only = True, view_name='details-detail')
    class Meta:
        model = Actor
        fields = ['name', 'details']

