# Generated by Django 3.2.16 on 2022-11-08 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_products', '0011_auto_20221101_1816'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0007_oldcart_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='guestCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('cancel', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_products.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
