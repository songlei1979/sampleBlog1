# Generated by Django 3.2.6 on 2021-08-31 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category1',
            new_name='category',
        ),
    ]
