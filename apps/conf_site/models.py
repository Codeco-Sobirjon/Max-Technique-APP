from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.translation import gettext as _


class ServiceName(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)

    objects = models.Manager()


class ServiceCarousel(models.Model):
    image = models.ImageField(upload_to='service/', null=True, blank=True, verbose_name="Изображение")
    service_name = models.ForeignKey(ServiceName, on_delete=models.CASCADE, null=True, blank=True,
                                     verbose_name="Услуга", related_name="service_name")

    def __str__(self):
        return self.service_name.name

    def save(self, *args, **kwargs):

        if not self.service_name:

            last_service_name = ServiceName.objects.last()
            if last_service_name:
                self.service_name = last_service_name

        super().save(*args, **kwargs)

    objects = models.Manager()

    class Meta:
        verbose_name = '1. Карусель услуг'
        verbose_name_plural = '1. Карусель услуг'


class Service(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name="Название услуга")
    description = models.TextField(null=True, blank=True, verbose_name="Краткое описание")
    created_at = models.DateField(auto_now_add=True, null=True, blank=True, verbose_name="Дата публикации")

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name = _("2. Услугм")
        verbose_name_plural = _("2. Услуги")


class RequirementService(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True, verbose_name="Краткое описание")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True,
                                verbose_name="Услугм", related_name="service_req")

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Требование к обслуживанию")
        verbose_name_plural = _("Требование к обслуживанию")


class PlaceOrder(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True, verbose_name="Имя")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон")
    msg = models.TextField(null=True, blank=True, verbose_name="Сообщение")

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name = _("3. Разместить заказ")
        verbose_name_plural = _("3. Разместить заказ")


class PlaceOrderService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Услуга")
    place_order = models.ForeignKey(PlaceOrder, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name="Заказ", related_name='place_order_service')

    objects = models.Manager()

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = _("Выбранная услуга")
        verbose_name_plural = _("Выбранная услуга")


class SeoDetails(models.Model):
    title = models.CharField(max_length=255, help_text="SEO-заголовок для страницы или поста.")
    description = models.TextField(help_text="SEO-описание для страницы или поста, обычно около 150-160 символов.")
    keywords = models.CharField(max_length=255, blank=True, help_text="Кома-разделенный список SEO-ключевых слов.")

    class Meta:
        verbose_name = "5. SEO-детали"
        verbose_name_plural = "5. SEO-детали"

    def __str__(self):
        return self.title


class Contacts(models.Model):
    title = models.CharField(max_length=255, help_text="Заголовок")
    email = models.EmailField(null=True, blank=True, verbose_name="Электронная почта")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон")

    objects = models.Manager()

    class Meta:
        verbose_name = "4. Контакная информация"
        verbose_name_plural = "4. Контакная информация"

    def __str__(self):
        return self.title
