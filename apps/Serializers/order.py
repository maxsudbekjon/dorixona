from rest_framework import serializers
from apps.models.Order import RefillOrder,RefillItem,ExtraItem

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
    refill_items=RefillItemModelSerializer(many=True,write_only=True,required=False)
    extra_items=ExtraItemModelSerializer(many=True,write_only=True,required=False)
    class Meta:
        model = RefillOrder
        fields=[
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'delivery_type',
            'refill_items',
            'extra_items'
        ]
    def to_internal_value(self,data):
        refill_items=data.get('refill_items')
        if refill_items and isinstance(refill_items,dict):
            data['refill_items']=[refill_items]

        extra_items=data.get('extra_items')
        if extra_items and isinstance(extra_items,dict):
            data['extra_items']=[extra_items]
        return super().to_internal_value(data)

    def create(self, validated_data):
        print(validated_data)
        refill_data = validated_data.pop('refill_items',[])
        extra_item_data = validated_data.pop('extra_items',[])
        order=RefillOrder.objects.create(**validated_data)
        RefillItem.objects.bulk_create([
            RefillItem(order=order, **item)
            for item in refill_data
        ])

        ExtraItem.objects.bulk_create([
            ExtraItem(order=order, **item)
            for item in extra_item_data
        ])
        return order
