# Generated by Django 2.2.6 on 2019-10-06 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_purchase_clearance_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='clearance_status',
            field=models.CharField(default='select', max_length=20),
            preserve_default=False,
        ),
    ]
