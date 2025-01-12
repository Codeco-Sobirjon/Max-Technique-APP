from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from apps.conf_site.models import ServiceCarousel, ServiceName, PlaceOrder, PlaceOrderService, Service, SeoDetails


# @admin.register(ServiceName)
# class ServiceNameAdmin(admin.ModelAdmin):
#     pass


@admin.register(ServiceCarousel)
class ServiceCarouselAdmin(admin.ModelAdmin):
    list_display = ['id', 'service_name__name']
    fields = ['image']


class PlaceOrderServiceTabularInline(admin.TabularInline):
    model = PlaceOrderService
    extra = 1
    fields = ['service']


class ServiceNameFilter(admin.SimpleListFilter):
    title = _('Название услуга')
    parameter_name = 'service_name'

    def lookups(self, request, model_admin):
        return [(service.id, service.name) for service in Service.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(placeorderservice__service_id=self.value())
        return queryset


@admin.register(PlaceOrder)
class PlaceOrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'phone', 'email']
    list_filter = [ServiceNameFilter]
    inlines = [PlaceOrderServiceTabularInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(SeoDetails)
class SeoDetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'keywords']

