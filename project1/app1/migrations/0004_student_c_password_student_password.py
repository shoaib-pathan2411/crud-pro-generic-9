# Generated by Django 4.1.4 on 2022-12-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_student_roll'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='c_password',
            field=models.CharField(default=1234, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default=1234, max_length=15),
            preserve_default=False,
        ),
    ]
