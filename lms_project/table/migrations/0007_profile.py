# Generated by Django 3.0.5 on 2021-05-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0006_auto_20210506_0103'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.TextField(max_length=200)),
                ('publications', models.CharField(max_length=70)),
                ('courses', models.CharField(max_length=70)),
            ],
        ),
    ]
