# Generated by Django 5.0.6 on 2024-07-20 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('questions_attempted', models.CharField(max_length=255)),
                ('percentage_score', models.CharField(max_length=255)),
                ('name', models.CharField(default='Anonymous2024-07-20', max_length=255)),
            ],
        ),
    ]
