# Generated by Django 4.2.16 on 2024-10-13 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='get',
            new_name='gst',
        ),
    ]
