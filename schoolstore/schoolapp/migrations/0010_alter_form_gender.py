# Generated by Django 4.1.3 on 2023-06-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0009_alter_form_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='gender',
            field=models.CharField(max_length=15),
        ),
    ]
