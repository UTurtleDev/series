# Generated by Django 4.2.5 on 2023-09-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('seen_seasons', models.IntegerField(default=0)),
                ('number_of_seasons', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
