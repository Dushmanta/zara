# Generated by Django 3.2.16 on 2022-11-13 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_products', '0012_auto_20221113_1758'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='offer',
            field=models.FloatField(default=0),
        ),
    ]
