from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext as _
from apps.conf_site.models import ServiceCarousel, ServiceName, PlaceOrder, PlaceOrderService, Service, SeoDetails, \
    RequirementService, Contacts

try:
    admin.site.unregister(Group)
except admin.sites.NotRegistered:
    pass

# @admin.register(ServiceName)
# class ServiceNameAdmin(admin.ModelAdmin):
#     pass


@admin.register(ServiceCarousel)
class ServiceCarouselAdmin(admin.ModelAdmin):
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


class RequirementServiceTabularInline(admin.TabularInline):
    model = RequirementService
    extra = 1
    fields = ['name']

    formfield_overrides = {
        models.CharField: {'widget': forms.Textarea(attrs={'cols': 40, 'rows': 3})}
    }


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    inlines = [RequirementServiceTabularInline]


@admin.register(SeoDetails)
class SeoDetailsAdmin(admin.ModelAdmin):
    list_display = ['title', 'keywords']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone']


admin.site.site_header = "Панель администратора"
admin.site.site_title = "Мой административный портал"
admin.site.index_title = "Добро пожаловать в панель управление"

