# Generated by Django 3.2.8 on 2021-11-01 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.CharField(max_length=3)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
