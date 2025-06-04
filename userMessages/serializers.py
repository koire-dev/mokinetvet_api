from rest_framework import serializers

from userMessages.models import UserMessage


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = '__all__'
        read_only_fields = ['id', 'sent_at', 'sender']
