# Generated by Django 4.0.2 on 2022-02-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_house_alter_watching_options_alter_watching_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='finch',
            name='houses',
            field=models.ManyToManyField(to='main_app.House'),
        ),
    ]
