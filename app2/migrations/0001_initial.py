# Generated by Django 2.0.8 on 2020-05-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('salary', models.IntegerField()),
                ('status', models.BooleanField()),
            ],
        ),
    ]
