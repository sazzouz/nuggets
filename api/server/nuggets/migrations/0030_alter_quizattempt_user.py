# Generated by Django 3.2.6 on 2021-08-19 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nuggets', '0029_alter_quizattempt_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizattempt',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
