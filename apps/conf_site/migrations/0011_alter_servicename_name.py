# Generated by Django 5.1.4 on 2025-01-15 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf_site', '0010_alter_requirementservice_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicename',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Карусельный раздел на сайте'),
        ),
    ]
