# Generated by Django 4.1.1 on 2022-09-13 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_project_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(default="The best project"),
            preserve_default=False,
        ),
    ]