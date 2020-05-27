from rest_framework import serializers

from core.models import Quizz


class QuizzSerializer(serializers.ModelSerializer):
    """Serialize a recipe"""

    class Meta:
        model = Quizz
        fields = ('id', 'title', 'description',)
        read_only_fields = ('id', 'title', 'description')
