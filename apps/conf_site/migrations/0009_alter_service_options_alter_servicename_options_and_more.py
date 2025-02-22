# Generated by Django 5.1.4 on 2025-01-15 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_site', '0008_alter_placeorder_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-id'], 'verbose_name': '2. Услуги', 'verbose_name_plural': '2. Услуги'},
        ),
        migrations.AlterModelOptions(
            name='servicename',
            options={'verbose_name': 'Услуги', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='seodetails',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, verbose_name='SEO-ключевых слов.'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='название услуги'),
        ),
    ]
