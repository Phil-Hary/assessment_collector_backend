# Generated by Django 5.0.3 on 2024-03-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_form_config_form_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsevalue',
            name='type',
            field=models.CharField(choices=[('STRING', 'STRING'), ('BOOL', 'BOOL'), ('INT', 'INT'), ('DATE', 'DATE')], max_length=10),
        ),
        migrations.AlterField(
            model_name='responsevalue',
            name='value',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
