# Generated by Django 4.1.5 on 2023-02-17 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_ticket_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='reviewed',
        ),
    ]
