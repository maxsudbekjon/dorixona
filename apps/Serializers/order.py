from rest_framework import serializers
from apps.models.Order import RefillOrder,RefillItem,ExtraItem
import requests
from django.conf import settings

bot_token = settings.TELEGRAM_BOT_TOKEN
chat_id = settings.TELEGRAM_CHAT_ID


class RefillItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=RefillItem
        fields=('rx_number',)

class ExtraItemModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExtraItem
        fields=[
            'name',
            'quantity'
        ]




class RefillOrderModelSerializer(serializers.ModelSerializer):
    refill_items = RefillItemModelSerializer(many=True, write_only=True, required=False)
    extra_items = ExtraItemModelSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = RefillOrder
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'delivery_type',
            'refill_items',
            'extra_items'
        ]

    def to_internal_value(self, data):
        refill_items = data.get('refill_items')
        if refill_items and isinstance(refill_items, dict):
            data['refill_items'] = [refill_items]

        extra_items = data.get('extra_items')
        if extra_items and isinstance(extra_items, dict):
            data['extra_items'] = [extra_items]
        return super().to_internal_value(data)

    def create(self, validated_data):
        refill_data = validated_data.pop('refill_items', [])
        extra_item_data = validated_data.pop('extra_items', [])

        order = RefillOrder.objects.create(**validated_data)

        RefillItem.objects.bulk_create([
            RefillItem(order=order, **item)
            for item in refill_data
        ])

        ExtraItem.objects.bulk_create([
            ExtraItem(order=order, **item)
            for item in extra_item_data
        ])

        self.send_telegram_message(order, refill_data, extra_item_data)

        return order

    def send_telegram_message(self, instance, refill_data, extra_item_data):
        """
        Function to send full order details to Telegram
        """

        # --- Basic Information ---
        text = (
            f"📦 <b>New Refill Order</b>\n\n"
            f"👤 <b>Customer:</b> {instance.first_name} {instance.last_name}\n"
            f"📞 <b>Phone:</b> {instance.phone_number}\n"
            f"📧 <b>Email:</b> {instance.email}\n"
            f"🚚 <b>Delivery Type:</b> {instance.delivery_type}\n"
        )

        # --- Refill Items ---
        if refill_data:
            text += "\n🔄 <b>Refill Items:</b>\n"
            for i, item in enumerate(refill_data, 1):
                # Format key-value pairs (e.g., service: ..., count: ...)
                item_str = ", ".join([f"{key}: {value}" for key, value in item.items()])
                text += f"{i}. {item_str}\n"

        # --- Extra Items ---
        if extra_item_data:
            text += "\n➕ <b>Extra Items:</b>\n"
            for i, item in enumerate(extra_item_data, 1):
                item_str = ", ".join([f"{key}: {value}" for key, value in item.items()])
                text += f"{i}. {item_str}\n"

        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

        try:
            response = requests.post(url, data={
                "chat_id": chat_id,
                "text": text,
                "parse_mode": "HTML"
            })
            if response.status_code != 200:
                print(f"Telegram error: {response.text}")
        except Exception as e:
            print(f"Telegram connection error: {e}")