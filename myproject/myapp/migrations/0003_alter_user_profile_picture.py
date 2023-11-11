# Generated by Django 4.2.7 on 2023-11-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_alter_user_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/profile_pics"
            ),
        ),
    ]
