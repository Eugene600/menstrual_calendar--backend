# Generated by Django 4.2.6 on 2024-11-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cycles',
            name='ovulation',
            field=models.DateField(default='2024-11-19'),
            preserve_default=False,
        ),
    ]
