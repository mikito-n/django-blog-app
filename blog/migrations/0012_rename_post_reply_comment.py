# Generated by Django 4.1.1 on 2022-11-07 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0011_alter_reply_post"),
    ]

    operations = [
        migrations.RenameField(
            model_name="reply", old_name="post", new_name="comment",
        ),
    ]
