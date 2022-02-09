# Generated by Django 4.0.2 on 2022-02-09 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_finch_options_watching'),
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='watching',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='watching',
            name='date',
            field=models.DateField(verbose_name='viewing date'),
        ),
    ]
