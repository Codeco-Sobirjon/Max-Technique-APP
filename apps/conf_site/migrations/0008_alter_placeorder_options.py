# Generated by Django 5.1.4 on 2025-01-15 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conf_site', '0007_alter_seodetails_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeorder',
            options={'ordering': ['-id'], 'verbose_name': '3. Заявки', 'verbose_name_plural': '3. Заявки'},
        ),
    ]
