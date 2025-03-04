# Generated by Django 5.0.7 on 2024-09-01 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_user_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='api.project'),
        ),
        migrations.AlterField(
            model_name='user',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='api.project'),
        ),
    ]
