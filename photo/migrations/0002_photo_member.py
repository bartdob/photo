# Generated by Django 3.2.3 on 2021-05-22 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_membership_type'),
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='member',
            field=models.ForeignKey(default='Basic', on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
