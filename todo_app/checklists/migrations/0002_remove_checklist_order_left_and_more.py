# Generated by Django 4.2.4 on 2023-09-01 22:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checklists", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="checklist",
            name="order_left",
        ),
        migrations.RemoveField(
            model_name="checklist",
            name="order_right",
        ),
        migrations.AddField(
            model_name="checklist",
            name="order",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
