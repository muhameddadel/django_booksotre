# Generated by Django 4.2 on 2023-05-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="post_code",
        ),
        migrations.AddField(
            model_name="order",
            name="country_code",
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name="order",
            name="email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="order",
            name="payment_option",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="order",
            name="postal_code",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.CharField(max_length=100),
        ),
    ]