# Generated by Django 5.0.6 on 2024-07-21 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='name',
            field=models.CharField(default='Anonymous2024-07-21', max_length=255),
        ),
    ]