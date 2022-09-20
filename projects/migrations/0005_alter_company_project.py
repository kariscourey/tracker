# Generated by Django 4.1.1 on 2022-09-20 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="project",
            field=models.ManyToManyField(
                null=True, related_name="companies", to="projects.project"
            ),
        ),
    ]
