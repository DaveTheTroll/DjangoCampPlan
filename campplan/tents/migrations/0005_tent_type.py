# Generated by Django 4.1.1 on 2022-09-23 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tents", "0004_tent_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="tent",
            name="type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="tents.tenttype",
            ),
            preserve_default=False,
        ),
    ]