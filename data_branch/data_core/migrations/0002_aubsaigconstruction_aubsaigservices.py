# Generated by Django 2.0.3 on 2018-03-31 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AubsaigConstruction',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AubsaigServices',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
