# Generated by Django 5.1.1 on 2024-10-05 11:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_room_topic_room_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
        migrations.AddField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.topic'),
        ),
    ]
