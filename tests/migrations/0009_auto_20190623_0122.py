# Generated by Django 2.2.1 on 2019-06-22 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_testorder_contact_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
