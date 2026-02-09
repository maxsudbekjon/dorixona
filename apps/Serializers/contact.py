from rest_framework import serializers
from apps.models import ContactRequest
import requests
from django.conf import settings

bot_token = settings.TELEGRAM_BOT_TOKEN
chat_id = settings.TELEGRAM_CHAT_ID

class ContactRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactRequest
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)

        # Telegramga xabar yuborish
        self.send_telegram_message(instance)

        return instance

    def send_telegram_message(self, instance):


        text = (
            f"📩 New Contact Request\n\n"
            f"Service: {instance.service.title}\n\n"
            f"👤 Name: {instance.first_name}\n"
            f"📞 Phone: {instance.phone_number}\n"
            f"📧 Email: {instance.email}\n"
            f"📝 Message: {instance.message}"
        )

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

        requests.post(url, data={
            "chat_id": chat_id,
            "text": text
        })
