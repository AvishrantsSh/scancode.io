# Generated by Django 3.1.7 on 2021-03-30 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanpipe', '0005_project_input_sources'),
    ]

    operations = [
        migrations.AddField(
            model_name='codebaseresource',
            name='compliance_alert',
            field=models.CharField(blank=True, choices=[('ok', 'Ok'), ('warning', 'Warning'), ('error', 'Error'), ('missing', 'Missing')], editable=False, help_text='Indicates how the detected licenses in a codebase resource complies with provided policies.', max_length=10),
        ),
    ]