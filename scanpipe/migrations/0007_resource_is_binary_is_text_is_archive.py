# Generated by Django 3.2.1 on 2021-05-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanpipe', '0006_codebaseresource_compliance_alert'),
    ]

    operations = [
        migrations.AddField(
            model_name='codebaseresource',
            name='is_archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='codebaseresource',
            name='is_binary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='codebaseresource',
            name='is_text',
            field=models.BooleanField(default=False),
        ),
    ]