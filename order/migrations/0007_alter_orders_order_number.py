# Generated by Django 4.2.16 on 2024-10-13 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_rename_order_form_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]