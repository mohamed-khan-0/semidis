# Generated by Django 5.1.1 on 2024-10-05 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.AddField(
            model_name='room',
            name='topic',
            field=models.ManyToManyField(to='base.topic'),
        ),
    ]
