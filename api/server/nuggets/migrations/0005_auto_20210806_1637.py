# Generated by Django 3.2.6 on 2021-08-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuggets', '0004_auto_20210806_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Quiz', 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]