# Generated by Django 4.1.5 on 2023-02-04 21:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crud", "0002_topic_chatroom_host_message_chatroom_topic"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="chatroom",
            options={"ordering": ["-updated_at", "-created_at"]},
        ),
        migrations.AddField(
            model_name="chatroom",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
