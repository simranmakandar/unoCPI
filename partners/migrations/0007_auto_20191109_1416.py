# Generated by Django 2.2.2 on 2019-11-09 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0006_auto_20191101_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campuspartner',
            name='weitz_cec_part',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=6),
        ),
        migrations.AlterField(
            model_name='historicalcampuspartner',
            name='weitz_cec_part',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=6),
        ),
    ]