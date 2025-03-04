# Generated by Django 5.0.7 on 2024-09-01 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_user_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='api.project'),
        ),
    ]
