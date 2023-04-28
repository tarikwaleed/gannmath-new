# Generated by Django 4.2 on 2023-04-28 07:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration", "0002_alter_subscription_start_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="subscription",
            name="end_date",
        ),
        migrations.RemoveField(
            model_name="subscription",
            name="start_date",
        ),
        migrations.AddField(
            model_name="subscription",
            name="order_id",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subscription",
            name="payment_source",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="subscription",
            name="subscription_id",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
