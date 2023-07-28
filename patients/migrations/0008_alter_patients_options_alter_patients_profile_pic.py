# Generated by Django 4.2.3 on 2023-07-25 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_alter_patients_profile_pic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patients',
            options={'verbose_name': 'patient', 'verbose_name_plural': 'patients'},
        ),
        migrations.AlterField(
            model_name='patients',
            name='profile_pic',
            field=models.ImageField(default=None, upload_to='profile_pictures'),
        ),
    ]
