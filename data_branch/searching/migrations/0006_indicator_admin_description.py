# Generated by Django 2.0.3 on 2018-04-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searching', '0005_auto_20180320_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicator',
            name='admin_description',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
    ]
