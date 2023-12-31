# Generated by Django 4.1.7 on 2023-08-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("MAN", "MAN"), ("WOMAN", "WOMAN")],
                max_length=6,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
