# Generated by Django 4.1.5 on 2023-02-17 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_remove_ticket_reviewed'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookToReview',
        ),
        migrations.DeleteModel(
            name='TicketCreation',
        ),
        migrations.DeleteModel(
            name='TicketToReview',
        ),
    ]
