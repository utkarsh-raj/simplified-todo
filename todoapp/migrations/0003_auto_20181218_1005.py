# Generated by Django 2.1.4 on 2018-12-18 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20181218_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='password',
            field=models.CharField(default=1, help_text='Password', max_length=100),
        ),
    ]
