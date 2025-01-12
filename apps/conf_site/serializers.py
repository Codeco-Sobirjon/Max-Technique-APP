from django.shortcuts import get_object_or_404
from rest_framework import serializers

from apps.conf_site.models import (
    Service,
    ServiceCarousel,
    PlaceOrder,
    PlaceOrderService, ServiceName, SeoDetails
)


class ServiceNameListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceName
        fields = ['id', 'name']


class ServiceCarouselListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceCarousel
        fields = [
            'id', 'image'
        ]


class ServiceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'description'
        ]


class PlaceOrderListSerializer(serializers.ModelSerializer):
    service = ServiceListSerializer(read_only=True, many=True)
    service_list = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = PlaceOrder
        fields = ['name', 'email', 'phone', 'msg', 'service', 'service_list']

    def create(self, validated_data):
        service_list = validated_data.pop('service_list', [])

        place_order = PlaceOrder.objects.create(**validated_data)

        for service_id in service_list:
            service = get_object_or_404(Service, id=service_id)
            PlaceOrderService.objects.create(place_order=place_order, service=service)

        return place_order


class SeoDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = SeoDetails
        fields = [
            'id', 'title', 'description', 'keywords'
        ]

