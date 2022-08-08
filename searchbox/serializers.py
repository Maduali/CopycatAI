from rest_framework import serializers
from searchbox.models import Search

class searchboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ["name", "result", "media", "media_result"]