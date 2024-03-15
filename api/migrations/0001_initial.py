# Generated by Django 5.0.3 on 2024-03-13 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'forms',
            },
        ),
        migrations.CreateModel(
            name='FormResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.form')),
            ],
            options={
                'db_table': 'form_responses',
            },
        ),
        migrations.CreateModel(
            name='ResponseValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('field_name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('STRING', 'STRING'), ('BOOL', 'BOOL'), ('INT', 'INT')], max_length=10)),
                ('FormResponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='response_values', to='api.formresponse')),
            ],
            options={
                'db_table': 'response_values',
            },
        ),
    ]
