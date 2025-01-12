# Generated by Django 5.1.4 on 2025-01-12 07:53

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='')),
                ('msg', models.TextField(blank=True, null=True, verbose_name='')),
            ],
            options={
                'verbose_name': '3. Разместить заказ',
                'verbose_name_plural': '3. Разместить заказ',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True, verbose_name='Название услуга')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Краткое описание')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': '2. Услугм',
                'verbose_name_plural': '2. Услуги',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PlaceOrderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='place_order_service', to='conf_site.placeorder', verbose_name='')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='conf_site.service')),
            ],
        ),
    ]
