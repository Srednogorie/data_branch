# Generated by Django 2.0.3 on 2018-04-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_core', '0003_aubsaigtrend'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsbsismmanBacklog',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanCustinv',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanDeliv',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanEmpl',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanExports',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanImports',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanInvent',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanNeworders',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanPmi',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanPrices',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismmanProd',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanBacklog',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanBusact',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanDeliv',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanEmpl',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanExports',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanImports',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanInvent',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanInvsent',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanNeword',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanPmi',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsismnmanPrices',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsmarkitComposite',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsmarkitManufacturing',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UsbsmarkitServices',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UscscbConsumerConfidence',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UscscbExpectations',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UscscbPresentSituation',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UscsuomCurrent',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UscsuomExpectations',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UscsuomFiveyearinfex',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UscsuomOneyearinfex',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UscsuomSentiment',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usggdpmanu',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usggdpmdol',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usggdpmqoq',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usggdpmyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usggdpqanu',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usggdpqdol',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usggdpqqoq',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usggdpqyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicocpimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicocpimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicocpimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicopcepimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicopcepimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicopcepimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicoppimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicoppimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicoppimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicpimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicpimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usicpimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usiexportpimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usiexportpimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usiexportpimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usigdpctpimanu',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usigdpctpiqanu',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usihpimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usihpimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usihpimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usiimportpimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usiimportpimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usiimportpimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usipcepimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usipcepimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usipcepimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usippimind',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usippimmom',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usippimyoy',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usmfedrate',
            fields=[
                ('period', models.DateField(db_column='Period', primary_key=True, serialize=False)),
                ('value', models.DecimalField(blank=True, db_column='Value', decimal_places=2, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]