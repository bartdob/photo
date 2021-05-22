# Generated by Django 3.2.3 on 2021-05-22 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_membership_type'),
        ('photo', '0002_photo_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
