# Generated by Django 3.1.4 on 2020-12-21 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20201221_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='flag',
            field=models.CharField(choices=[('1', 'Enabled'), ('0', 'Disabled')], default='1', max_length=4),
        ),
    ]
