# Generated by Django 4.1.1 on 2022-09-23 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tents", "0002_alter_tent_notes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tent",
            name="colour",
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name="tent",
            name="name",
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="tent",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
