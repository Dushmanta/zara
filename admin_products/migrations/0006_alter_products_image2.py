# Generated by Django 3.2.16 on 2022-10-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_products', '0005_auto_20221023_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
