# Generated by Django 3.2.21 on 2023-10-24 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_deliveriinformation_basket_information'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveriinformation',
            name='basket_information',
            field=models.JSONField(),
        ),
    ]
