# Generated by Django 4.1.1 on 2022-10-15 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_rename_tag_post_tags"),
    ]

    operations = [
        migrations.RenameField(
            model_name="category", old_name="sulg", new_name="slug",
        ),
    ]