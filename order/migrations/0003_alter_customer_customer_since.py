# Generated by Django 4.2.16 on 2024-10-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_customer_customer_since'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_since',
            field=models.DateField(max_length=200, null=True),
        ),
    ]
