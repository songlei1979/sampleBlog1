# Generated by Django 3.2.6 on 2021-09-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='github_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/photo'),
        ),
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]