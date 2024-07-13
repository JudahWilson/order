# Generated by Django 5.0.6 on 2024-07-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0004_ticket_ticket_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgTicketCounter',
            fields=[
                ('orgid', models.IntegerField(primary_key=True, serialize=False)),
                ('last_ticket_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together={('organization', 'ticket_number')},
        ),
    ]