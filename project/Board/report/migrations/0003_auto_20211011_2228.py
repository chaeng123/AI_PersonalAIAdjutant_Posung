# Generated by Django 3.2.8 on 2021-10-11 22:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_report_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='content2',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='content3',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
