# Generated by Django 3.2.6 on 2021-08-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuggets', '0023_alter_quiz_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='metadata',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
    ]
