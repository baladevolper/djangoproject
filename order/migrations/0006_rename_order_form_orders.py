# Generated by Django 4.2.16 on 2024-10-13 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
        ('order', '0005_alter_customer_customer_since_order_form'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_form',
            new_name='Orders',
        ),
    ]
