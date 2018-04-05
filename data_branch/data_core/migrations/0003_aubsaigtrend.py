# Generated by Django 2.0.3 on 2018-04-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_core', '0002_aubsaigconstruction_aubsaigservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='AubsaigTrend',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('manufacturing', models.DecimalField(blank=True, db_column='Manufacturing', decimal_places=2, max_digits=12, null=True)),
                ('services', models.DecimalField(blank=True, db_column='Services', decimal_places=2, max_digits=12, null=True)),
                ('construction', models.DecimalField(blank=True, db_column='Construction', decimal_places=2, max_digits=12, null=True)),
            ],
        ),
    ]