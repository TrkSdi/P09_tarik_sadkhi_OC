# Generated by Django 4.1.5 on 2023-02-06 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]