# Generated by Django 5.1.4 on 2025-01-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_site', '0005_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seodetails',
            options={'verbose_name': '5. SEO-детали', 'verbose_name_plural': '5. SEO-детали'},
        ),
        migrations.AlterField(
            model_name='contacts',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
