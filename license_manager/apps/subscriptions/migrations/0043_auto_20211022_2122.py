# Generated by Django 3.2.8 on 2021-10-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0042_auto_20211022_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsubscriptionplan',
            name='should_auto_apply_licenses',
            field=models.BooleanField(blank=True, help_text='Whether licenses from this Subscription Plan should be auto applied.', null=True),
        ),
        migrations.AddField(
            model_name='subscriptionplan',
            name='should_auto_apply_licenses',
            field=models.BooleanField(blank=True, help_text='Whether licenses from this Subscription Plan should be auto applied.', null=True),
        ),
    ]
