# Generated by Django 2.2.2 on 2019-11-18 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20191114_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='edit_Projects_Form_Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1250)),
            ],
            options={
                'verbose_name': 'Edit Projects Form Snippet',
            },
        ),
    ]
