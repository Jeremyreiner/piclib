# Generated by Django 4.0 on 2021-12-22 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_remove_photo_image_photoimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PhotoImage',
        ),
    ]
