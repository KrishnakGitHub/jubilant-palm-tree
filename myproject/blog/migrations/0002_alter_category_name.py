# Generated by Django 4.2.7 on 2023-11-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                choices=[
                    ("Mental Health", "Mental Health"),
                    ("Heart Disease", "Heart Disease"),
                    ("Covid19", "Covid19"),
                    ("Immunization", "Immunization"),
                ],
                max_length=255,
            ),
        ),
    ]