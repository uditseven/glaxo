# Generated by Django 2.2.6 on 2019-10-06 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_purchase_purchase_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='clearance_status',
        ),
    ]
