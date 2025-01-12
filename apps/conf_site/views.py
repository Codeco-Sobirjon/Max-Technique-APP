from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.conf_site.models import (
    Service,
    ServiceCarousel,
    PlaceOrder,
    PlaceOrderService, ServiceName, SeoDetails
)
from apps.conf_site.serializers import ServiceCarouselListSerializer, ServiceListSerializer, PlaceOrderListSerializer, \
    SeoDetailsSerializer


class ServiceCarouselListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['Service Carousel'],
        operation_description="Retrieve the list of service carousel items.",
        responses={
            200: ServiceCarouselListSerializer(many=True),
            400: openapi.Response('Bad Request'),
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            queryset = ServiceCarousel.objects.all()

            serializer = ServiceCarouselListSerializer(queryset, many=True, context={
                'request': request
            })
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class ServiceListAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['Service'],
        responses={200: ServiceListSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):

        services = Service.objects.all()
        serializer = ServiceListSerializer(services, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlaceOrderCreateAPIView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['Place Order'],
        request_body=PlaceOrderListSerializer,
        responses={201: PlaceOrderListSerializer, 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):

        serializer = PlaceOrderListSerializer(data=request.data)

        if serializer.is_valid():
            place_order = serializer.save()
            return Response({'msg': "Successfull created"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SeoDetailsListView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['Seo Details'],
        operation_description="Retrieve a list of all SEO details",
        responses={200: SeoDetailsSerializer(many=True)},
    )
    def get(self, request):
        seo_details = SeoDetails.objects.all()
        serializer = SeoDetailsSerializer(seo_details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
