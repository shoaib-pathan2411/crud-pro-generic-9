# Generated by Django 4.1.4 on 2022-12-21 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birth_date',
            field=models.DateField(default='2000-12-12'),
            preserve_default=False,
        ),
    ]