# Generated by Django 4.1.1 on 2022-11-07 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_remove_historicalproject_mission_area_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subcategory',
            field=models.ManyToManyField(to='projects.subcategory'),
        ),
    ]