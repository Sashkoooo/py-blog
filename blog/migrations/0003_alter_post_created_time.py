# Generated by Django 4.1 on 2023-06-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_alter_commentary_created_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="created_time",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
