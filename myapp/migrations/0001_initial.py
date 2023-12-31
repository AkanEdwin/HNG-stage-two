# Generated by Django 3.2.21 on 2023-09-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birthdate', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('track', models.CharField(max_length=20)),
            ],
        ),
    ]
