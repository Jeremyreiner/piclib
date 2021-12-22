# Generated by Django 4.0 on 2021-12-21 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('photos', '0003_photo_timestamp_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='photo_profile', to='auth.user'),
            preserve_default=False,
        ),
    ]
